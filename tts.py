# tts : text to speech
# stt : speech to text

from gtts import gTTS

text='대화 모드입니다'
tts_en=gTTS(text=text, lang='ko')

file_name='say3.mp3'
tts_en.save(file_name)

from playsound import playsound
playsound(file_name)


#한글
#text='한글'
#tts_ko=gTTS(text=text, lang='ko')

#file_name='sample.mp3'
#tts_ko.save(file_name)

#from playsound import playsound
#playsound(file_name)



# 긴 문장
# with open('sample.txt','r',encoding='utf8') as f:
  #   text=f.read()
# tts_ko=gTTS(text=text, lang='ko')
# file_name='sample.mp3'
# tts_ko.save(file_name)
# from playsound import playsound
# playsound(file_name)
