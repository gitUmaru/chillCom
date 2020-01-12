import io
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.shortcuts import render
from google.cloud import vision
from face_dect.models import history
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
from io import BytesIO
from django.utils.http import urlsafe_base64_decode

# Create your views here.
def index(request):
    return render(request,'index.html')

def info(request):
    #vision api code which also saves data to db.
    vision_client = vision.ImageAnnotatorClient()

    pic = request.POST["pic"]
    format, imgstr = pic.split(';base64,')
    myfile = base64.b64decode(imgstr)
    imageFile = BytesIO(myfile)

    image = vision.types.Image(content=imageFile.read())
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
    #record=history(url=file_name,data=label_data)
    #record.save()
    return render(request,'results.html',{"labels":labels,'image':imageFile})

def getHistory(request):
    #Getting history from db.
    previous_searches=history.objects.all()
    return render(request,'history.html',{"data":previous_searches})


def chat(request):
    return render(request, 'chat.html')

def main(request):
    return render(request, 'main.html')
    
def animation(request):
    return render(request, 'animation.html')
    
def welcome(request):
    return render(request, 'welcome.html')
    
def music_playlist(request):
    return render(request, 'music_playlist.html')

