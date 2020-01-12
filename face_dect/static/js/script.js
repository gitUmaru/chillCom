var hidden_canvas = document.querySelector("canvas");
var video = document.querySelector("#videoElement");
var takepicture_button = document.getElementById("startbutton");
takepicture_button.addEventListener("click", takepicture);

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function(stream) {
      video.srcObject = stream;
    })
    .catch(function(err0r) {
      console.log("Something went wrong!");
    });
}

function takepicture() {
  (video = document.querySelector("#videoElement")),
    (image = document.getElementById("dl-btn")),
    (width = video.videoWidth / 3),
    (height = video.videoHeight / 3),
    (context = hidden_canvas.getContext("2d"));
  hidden_canvas.width = width;
  hidden_canvas.height = height;
  context.drawImage(video, 0, 0, width, height);
}
