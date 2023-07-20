# pip install SpeechRecognition
# pip install PyAudio

import speech_recognition as sr

#리커그나이저 객체 r 선언
r = sr.Recognizer()

#마이크
with sr.Microphone() as source:
    print('듣고잇다')
    audio = r.listen(source) # 마이크로부터 음성 듣기
    
try:
    #구글api로인식 (하루50회)
    text = r.recognize_google(audio, language='ko') # 한글은 ko
    #text = r.recognize_tensorflow(audio, language='en-US') # 한글은 ko
    #text = r.recognize_bing(audio, language='en-US') # 한글은 ko
    print(text)
except sr.UnknownValueError:
    print('인식실패')
except sr.RequestError:
    print('요청실패: {0}'.format(e)) # api키오류 또는 네트워크단절등
        