from hugchat import hugchat
from hugchat.login import Login
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound

import os

#리커그나이저 객체 r 선언
r = sr.Recognizer()

email='hope69034@gmail.com'
passwd='!Ing12924103'

# Log in to huggingface and grant authorization to huggingchat
sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookies()

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) # or cookie_path="usercookies/<email>.json"



 # 새로운 파일 이름 생성
global count 
count = 1
global file_name
file_name='./sound/sample.mp3' # mp3로 ########

def filename_change():
  global file_name  
  global count 
  while os.path.exists(file_name):
      count += 1
      file_name = f'./sound/sample{count}.mp3'

#아웃풋도출def
#모델오버로딩에러처리 > 재귀용법으로 에러가 나도 무한try
def chatchat(a):
  try:
    print(3)
    output=chatbot.chat(a)
    print('bot: ',output)
    tts_en=gTTS(text=output, lang='en')
    filename_change()
    tts_en.save(file_name)  
    playsound(file_name)
  except:
    chatchat(a)
    
# 소리 인식    
def api():
      #구글api로인식
      print(0)
      text = r.recognize_google(audio, language='en-US') # 한글은 ko
      print(text)
      print(1)
      chatchat(text)
      print(2)
      # vosk 모델 사용
      #text = r.recognize_vosk(audio, language='en-US') # 한글은 ko
      #print(text)
      #chatchat(text)
    
    
#마이크로 소리 받기    
    
while True: 
  #마이크
  with sr.Microphone() as source:
      print('say someting')
      audio = r.listen(source) # 마이크로부터 음성 듣기
      
  try:
      api()
  except sr.UnknownValueError:
      print('인식실패')
  except sr.RequestError:
      print('요청실패: {0}'.format(e)) # api키오류 또는 네트워크단절등
    

# Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# Get conversation list
# conversation_list = chatbot.get_conversation_list()