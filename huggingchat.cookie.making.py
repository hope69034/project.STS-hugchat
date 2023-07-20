# 한번 가동

from hugchat.login import Login

email=' '
passwd=' '
# login
sign = Login(email, passwd)
cookies = sign.login()
sign.saveCookiesToDir()

# load cookies from usercookies/<email>.json
sign = Login(email, None)
cookies = sign.loadCookiesFromDir() # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.