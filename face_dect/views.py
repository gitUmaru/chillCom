import io
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.shortcuts import render
from google.cloud import vision
from face_dect.models import history


var = 'alksdalskdjlaskd'

# Create your views here.
def index(request):
    return render(request,'index.html')

def info(request):
    #vision api code which also saves data to db.
    vision_client = vision.ImageAnnotatorClient()
    myfile = request.FILES["pic"]
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    file_name = fs.url(filename)
    with io.open(file_name, "rb") as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    #labels = image.detect_labels()
    #label_data=""
    response = vision_client.face_detection(image=image)
    labels = response.face_annotations
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    label_data = ''
    print(type(labels))
    for label in labels:
        print('anger: {}'.format(likelihood_name[label.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[label.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[label.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in label.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))
    record=history(url=file_name,data=label_data)
    record.save()
    return render(request,'results.html',{"labels":labels,'image':file_name})

def getHistory(request):
    #Getting history from db.
    previous_searches=history.objects.all()
    return render(request,'history.html',{"data":previous_searches})
