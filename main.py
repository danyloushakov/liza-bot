import os
import telebot
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello from LizaBot", 200

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=['start'])
def start_handler(message):
    voice = open('audio/privit.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['шепочи'])
def shepochy_handler(message):
    voice = open('audio/shepochy.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

# додаєш інші команди аналогічно

if __name__ == "__main__":
    # Видаляємо старий webhook (на всякий випадок)
    bot.remove_webhook()
    # Ставимо новий webhook
    bot.set_webhook(url=f"https://liza-bot.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=8080)
