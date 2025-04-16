import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привіт, мій Котуся… Я чекала тебе.")
    bot.send_voice(message.chat.id, voice=open('liza_welcome.ogg', 'rb'))

bot.polling()