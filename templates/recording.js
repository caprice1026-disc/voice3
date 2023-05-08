const recognition = new webkitSpeechRecognition();
recognition.language = "ja-JP";
recognition.continuous = true;
recognition.onresult = ({ results }) => {
  const output = document.querySelector(".output");
  output.textContent = results[0][0].transcript;
  const text = output.textContent;
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/process-text', true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.send(`text=${text}`);
};

const recordButton = document.querySelector("#record-button");
const stopButton = document.querySelector("#stop-button");

function startRecording() {
  recognition.start();
  recordButton.disabled = true;
  stopButton.disabled = false;
}

function stopRecording() {
  recognition.stop();
  recordButton.disabled = false;
  stopButton.disabled = true;
}

recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);