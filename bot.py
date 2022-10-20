# 
# Name: Link Remover Telegram Bot
# Author: Max Base
# Date: 2022/10/20
# Repository: https://github.com/BaseMax/LinkRemoverTelegramBot
# 

from telebot import TeleBot

# config
TOKEN = '5592542597:AAFZyzDCL8wNPlYNzR8fzh8wxAS0tVkxUn4'

# setup
app = TeleBot(TOKEN)

# listener
@app.message_handler(func=lambda message: True)
def echo_all(message):
    if 'http://' in message.text or 'https://' in message.text:
        # app.reply_to(message, 'URL detected')
        app.delete_message(message.chat.id, message.message_id)

# keep alive
if __name__ == '__main__':
    app.infinity_polling()
