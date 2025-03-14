import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler

# Настраиваем Flask
app = Flask(__name__)

# Получаем токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Например, https://your-app.onrender.com/webhook

if not BOT_TOKEN or not WEBHOOK_URL:
    raise ValueError("Ошибка: Необходимо задать BOT_TOKEN и WEBHOOK_URL в переменных окружения.")

bot = Bot(token=BOT_TOKEN)

# Создаём обработчик команд
async def start(update: Update, context):
    await update.message.reply_text("Привет! Бот работает через вебхук.")

# Создаём объект Telegram-бота
app_bot = Application.builder().token(BOT_TOKEN).build()
app_bot.add_handler(CommandHandler("start", start))

# Устанавливаем webhook
@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    bot.set_webhook(url=WEBHOOK_URL)
    return "Webhook установлен!", 200

# Обрабатываем входящие запросы от Telegram
@app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json()
    update = Update.de_json(data, bot)
    await app_bot.process_update(update)
    return "OK", 200

# Главный запуск сервера Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
