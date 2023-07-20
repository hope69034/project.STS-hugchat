from hugchat import hugchat
from hugchat.login import Login
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound

import pygame
import os

# 번역
from translate import Translator
#영어를 한글로
def translate_english_to_korean(text):
    translator = Translator(to_lang='ko', from_lang='en')
    translation = translator.translate(text)
    return translation
#한글을 영어로
def translate_korean_to_english(text):
    translator = Translator(to_lang='en', from_lang='ko')
    translation = translator.translate(text)
    return translation


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
    output = translate_korean_to_english(a) # Translate
    #output = translate_english_to_korean(a) # Translate
    print('Translate : ',output)
    tts_en=gTTS(text=output, lang='en')
    #tts_en=gTTS(text=output, lang='ko')  
    filename_change()
    tts_en.save(file_name)  
    #playsound(file_name)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    # Close the audio file
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
  except:
    chatchat(a)
    


# 소리 인식    
def api():
      #구글 활용
      text = r.recognize_google(audio, language='ko')  
      print(text)
      #chatchat(text)
      #vosk 모델 활용
      #text = r.recognize_vosk(audio, language='en-US') 
      #print('User:',text[14:-3])
      chatchat(text)
    
def intro():
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('./say.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        # Close the audio file
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()








#마이크로 소리 받기    
    
while True: 
  #마이크
  with sr.Microphone() as source:
    print('<<<<<<<<<<<<<<<< 음성을 기다리고 있습니다. >>>>>>>>>>>>>>>>')
    #intro()
    audio = r.listen(source) # 마이크로부터 음성 듣기
        
  try:
      api()
  except sr.UnknownValueError:
      #print('인식실패')
      print('<<<<<<<<<<<<<<<< 음성을 기다리고 있습니다. >>>>>>>>>>>>>>>>')
  except sr.RequestError:
      print('요청실패: {0}'.format(e)) # api키오류 또는 네트워크단절등
    

# Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# Get conversation list
# conversation_list = chatbot.get_conversation_list()












