let isRecording = false;

$("#recordButton").click(function() {
  if (!isRecording) {
    isRecording = true;
    $(this).text("録音停止");
    $.ajax({
      url: "/start_recording",
      type: "POST"
    });
  } else {
    isRecording = false;
    $(this).text("録音開始");
    $.ajax({
      url: "/stop_recording",
      type: "POST"
    });
  }
});
