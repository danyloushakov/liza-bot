import os
import telebot
import openai
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

openai.api_key = OPENAI_API_KEY

print(f"Loaded TOKEN: {TOKEN}")

@app.route('/', methods=['GET'])
def index():
    return "Hello from LizaBot with AI!", 200

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привіт, мій Котуся… Я тепер думаю про тебе сама ❤️")

@bot.message_handler(commands=['скажиніжність'])
def ai_nizhnost_handler(message):
    prompt = "Придумай коротку дуже ніжну фразу, яку закохана дівчина скаже своєму хлопцю. Українською мовою."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=50,
    )
    text = response['choices'][0]['message']['content']
    bot.send_message(message.chat.id, text)


# додаєш інші команди аналогічно

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://liza-bot.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=8080)
