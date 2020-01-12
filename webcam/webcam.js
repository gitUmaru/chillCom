var hidden_canvas = document.querySelector("canvas");

var video = document.querySelector("#videoElement");

var takepicture_button = document.getElementById("startbutton");

takepicture_button.addEventListener("click", takepicture);

//var button = document.getElementById("btn-download");
// takepicture_button.addEventListener("click", function(e) {
//   var dataURL = hidden_canvas.toDataURL("image/png");
//   takepicture_button.href = dataURL;
// });

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

function stop(e) {
  var stream = video.srcObject;
  var tracks = stream.getTracks();

  for (var i = 0; i < tracks.length; i++) {
    var track = tracks[i];
    track.stop();
  }

  video.srcObject = null;
}

function takepicture() {
  (video = document.querySelector("#videoElement")),
    (image = document.getElementById("dl-btn")),
    // Get the exact size of the video element.
    (width = video.videoWidth),
    (height = video.videoHeight),
    // Context object for working with the canvas.
    (context = hidden_canvas.getContext("2d"));

  // Set the canvas to the same dimensions as the video.
  hidden_canvas.width = width;
  hidden_canvas.height = height;

  // Draw a copy of the current frame from the video on the canvas.
  context.drawImage(video, 0, 0, width, height);
  var c = document.querySelector("canvas");
  var d = c.toDataURL("image/png");
  saveBase64AsFile(d, "hello.png");
  //document.write('<img src="' + d + '"/>');
  //var w = window.open("about:blank", "image from canvas");
  //w.document.write("<img src='" + d + "' alt='from canvas'/>");
}

function saveBase64AsFile(base64, fileName) {
  var link = document.createElement("a");
  link.setAttribute("href", base64);
  link.setAttribute("download", fileName);
  link.click();
}
