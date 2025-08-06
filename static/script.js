const frame = document.getElementById("video-frame");
const predictionText = document.getElementById("prediction");

// Create and configure hidden video element
const hiddenVideo = document.createElement("video");
hiddenVideo.setAttribute("autoplay", true);
hiddenVideo.setAttribute("playsinline", true);
hiddenVideo.style.display = "none"; // Optional: keep it hidden

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    hiddenVideo.srcObject = stream;
    hiddenVideo.onloadedmetadata = () => {
      hiddenVideo.play();
      requestAnimationFrame(sendFrameLoop);  // Start loop when video is ready
    };
  });

function sendFrameLoop() {
  if (hiddenVideo.videoWidth === 0 || hiddenVideo.videoHeight === 0) {
    // Video not ready yet, try again
    requestAnimationFrame(sendFrameLoop);
    return;
  }

  const canvas = document.createElement("canvas");
  canvas.width = hiddenVideo.videoWidth;
  canvas.height = hiddenVideo.videoHeight;
  const ctx = canvas.getContext("2d");
  ctx.drawImage(hiddenVideo, 0, 0);

  const dataURL = canvas.toDataURL("image/jpeg");

  fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image: dataURL })
  })
  .then(response => response.json())
  .then(data => {
    predictionText.innerText = `Prediction: ${data.prediction || '...'}`;
    if (data.image) {
      frame.src = data.image;
    }
  })
  .finally(() => {
    requestAnimationFrame(sendFrameLoop);  // Continue the loop
  });
}
