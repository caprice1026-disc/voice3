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
"始まった時の処理について"
const start = document.querySelector(".start");
start.addEventListener("click", () => {
  recognition.start();
});
"終わった時の処理について"
const stop = document.querySelector(".stop");
stop.addEventListener("click", () => {
  recognition.stop();
});