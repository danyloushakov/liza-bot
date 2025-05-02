import os
import telebot
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    voice = open('audio/privit.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['шепочи'])
def shepochy_handler(message):
    voice = open('audio/shepochy.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['сіські'])
def siski_handler(message):
    voice = open('audio/privit.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['ревную'])
def revnuyu_handler(message):
    voice = open('audio/revnuyu.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['наливай'])
def nalivay_handler(message):
    voice = open('audio/nalivay.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['сон'])
def son_handler(message):
    voice = open('audio/son.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

keep_alive()
bot.polling(non_stop=True)
