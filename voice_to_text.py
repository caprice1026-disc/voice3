import io
from io import BytesIO
import openai
import pyaudio
import wave
import tempfile


openai.api_key = "your_openai_api_key"
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5

def record_audio():

    # 音声録音
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
#出力先は後で変えるようにする
    print("録音中だよ～")
    frames = []
    for _ in range(0, int(RATE / CHUNK * 30)):
     data = stream.read(CHUNK)
     frames.append(data)
#出力先は後で変えるようにする
    print("録音終了")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames, p

#音声をバイナリデータに変換
def audio_to_text(frames, p):
    audio_data = io.BytesIO()
    wave_write = wave.open(audio_data, 'wb')
    wave_write.setnchannels(CHANNELS)
    wave_write.setsampwidth(p.get_sample_size(FORMAT))
    wave_write.setframerate(RATE)
    wave_write.writeframes(b''.join(frames))
    wave_write.close()

#whisper-1使う
    audio_file = audio_data.getvalue()
    text = openai.Audio.transcribe("whisper-1", file=audio_file)
#出力先は後で変えるようにする
    return text

frames, p = record_audio()
text = audio_to_text(frames, p)



