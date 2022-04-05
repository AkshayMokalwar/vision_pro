// camera stream video element
let on_stream_video = document.querySelector('#camera-stream');
// flip button element
let flipBtn = document.querySelector('#flip-btn');
var snapshot = document.getElementById( "canvas" );
// default user media options
let constraints = { audio: false, video: true }
let shouldFaceUser = true;

// check whether we can use facingMode
let supports = navigator.mediaDevices.getSupportedConstraints();
if( supports['facingMode'] === true ) {
  flipBtn.disabled = false;
}

let stream = null;

function capture() {
  constraints.video = {
      width: {
        min: 640,
        ideal: 640,
        max: 1280,
      },
    height: {
      min: 360,
      ideal: 360,
      max: 720
    },
    facingMode: shouldFaceUser ? 'user' : 'environment'
  }
  navigator.mediaDevices.getUserMedia(constraints)
    .then(function(mediaStream) {
      stream  = mediaStream;
      on_stream_video.srcObject = stream;
      on_stream_video.play();
    })
    .catch(function(err) {
      console.log(err)
    });
}

flipBtn.addEventListener('click', function(){
  if( stream == null ) return
  // we need to flip, stop everything
  stream.getTracks().forEach(t => {
    t.stop();
  });
  // toggle / flip
  shouldFaceUser = !shouldFaceUser;
  capture();
})

capture();
document.getElementById("capture-camera").addEventListener("click", function() {
  // Elements for taking the snapshot
    const video = document.getElementById("camera-stream");
    var canvas = document.getElementById('canvas');
    
    canvas.width = 640;
    canvas.height =480;
    // alert(canvas.width);
    // alert(canvas.height);
    var k=canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let anchor = document.createElement("a");
    anchor.download = "download." + "jpg";
    anchor.href = k.toDataURL("image/jpg");
    // alert(anchor.href);
    anchor.click(); 
    
    
 

});