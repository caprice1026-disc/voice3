import os
import requests
import json
import io
import wave
import pyaudio
import main2 as main
import app
import main2 as main

def post_audio_query(text: str) -> dict:
 response2 = main.main()
 params = {'text': response2, 'speaker': 1}
 res = requests.post('http://localhost:50021/audio_query', json=params)
 return res.json()

def post_synthesis(audio_query_response: dict) -> bytes:
   params = {'speaker':1}
   headers = {'Content-Type': 'application/json'}
   audio_query_response_json = json.dumps(audio_query_response)
   res = requests.post(
        'http://localhost:50021/synthesis',
        data=audio_query_response_json,
        params=params,
        headers=headers
    )
   return res.content

def play_wav(wav_file: bytes):
    wr: wave.Wave_read = wave.open(io.BytesIO(wav_file))
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wr.getsampwidth()),
        channels=wr.getnchannels(),
        rate=wr.getframerate(),
        output=True
    )
    chunk = 1024
    data = wr.readframes(chunk)
    while data:
        stream.write(data)
        data = wr.readframes(chunk)
    stream.close()
    p.terminate()

def text_to_voice(text: str):
    res = post_audio_query(text)
    wav = post_synthesis(res)
    play_wav(wav)