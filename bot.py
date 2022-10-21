# 
# Name: Link Remover Telegram Bot
# Author: Max Base
# Date: 2022/10/20
# Repository: https://github.com/BaseMax/LinkRemoverTelegramBot
# 

from telebot import TeleBot

# config
TOKEN = '5592542597:AAFZyzDCL8wNPlYNzR8fzh8wxAS0tVkxUn4'
ADMINS = [
    '1215864830'
]

# setup
app = TeleBot(TOKEN)

def check_message(type, message):
    print(type, message)

    if message.from_user.id in ADMINS:
        return

    if message.text.find('@') != -1:
        print("Found username in message text")
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('t.me') != -1:
        print("Found link to username in message text")
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('http://') != -1 or message.text.find('https://') != -1:
        print("Found link to website in message text")
        app.delete_message(message.chat.id, message.message_id)

# edit message listener
@app.edited_message_handler(func=lambda message: True)
def edit_message(message):
    check_message("edit", message)

# new message listener
@app.message_handler(func=lambda message: True)
def new_message(message):
    check_message("new", message)

# keep alive
if __name__ == '__main__':
    app.infinity_polling()
