import speech_recognition as sr

# 리커그나이저 객체 r 선언
r = sr.Recognizer()

# 마이크에서 음성 입력 받기
with sr.Microphone() as source:
    print("말하세요...")
    audio = r.listen(source)  # 마이크로부터 음성 듣기

# 음성을 WAV 파일로 저장
with open("output.wav", "wb") as f:
    f.write(audio.get_wav_data())

# 저장한 파일 불러오기
with sr.AudioFile('output.wav') as source:
    audio = r.record(source)  # 파일로부터 음성 듣기

try:
    # 구글 API를 사용하여 인식
#    text = r.recognize_google(audio, language='en-US')  # 한글은 'ko'
    text = r.recognize_google(audio, language='ko')  # 한글은 'ko'
    print(text)
except sr.UnknownValueError:
    print('인식 실패')
except sr.RequestError as e:
    print('요청 실패: {0}'.format(e))  # API 키 오류 또는 네트워크 단절 등
