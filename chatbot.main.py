from hugchat import hugchat
from hugchat.login import Login

email='hope69034@gmail.com'
passwd='!Ing12924103'

# Log in to huggingface and grant authorization to huggingchat
sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookies()

# Create a ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) # or cookie_path="usercookies/<email>.json"

#아웃풋도출def함수
#모델오버로딩에러처리 > 재귀용법으로 에러가 나도 무한try
def chatchat(a):
  try:
    print('bot: ',chatbot.chat(a))
  except:
    chatchat(a)
    
while True: 
  print('say someting!!')
  chatchat(input('user: '))

# Create a new conversation
# id = chatbot.new_conversation()
# chatbot.change_conversation(id)

# Get conversation list
# conversation_list = chatbot.get_conversation_list()