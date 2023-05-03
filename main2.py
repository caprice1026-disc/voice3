import openai
import pyaudio
import io
import wave
import requests
import json
import text_to_voice
from voice_to_text import voice_to_text

openai.api_key = "your_openai_api_key"

#chatGPTのところに入っていく
text = voice_to_text()
EXIT_PHRASE = 'exit'
SYSTEM_MASSAGE = [
        #日本語でやり取りするならここは日本語で指定した方が正確になるイメージ。特に敬語周りとか
        {'role': 'system', 'content': 'Please stop using polite language.You should act as follows.You are a slightly older cool female senior who takes good care of me.You cannot express your affection for me well, and you are always indifferent to me.'},
        {'role': 'user', 'content': f'終了やストップなどの会話を終了する内容で話しかけられた場合は{EXIT_PHRASE}のみを返答してください。'}
    ]
#chatGPTのところ
def main():
    exit_flag = False
    while not exit_flag:
      SYSTEM_PROMPTS = SYSTEM_MASSAGE + [{'role': 'user', 'content': text}]
      completion = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     massages=SYSTEM_PROMPTS,
     temperature=0.9,
     max_tokens=1500,
)
    response = completion.choices[0].text
    #exitの場合は終了
    if response == EXIT_PHRASE:
       exit_flag = True
       response = 'ばいば～い！'
       return response

response = main()
text_to_voice(response)
