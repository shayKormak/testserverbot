import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Получаем токен из переменных окружения (чтобы не хранить его в коде)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен есть
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден! Укажите его в переменных окружения.")

# Функция обработки команды /start
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я простой Telegram-бот. Напиши мне что-нибудь!")

# Функция обработки команды /help
async def help_command(update: Update, context):
    await update.message.reply_text("Я умею отвечать на сообщения! Просто напиши мне что-нибудь.")

# Функция обработки обычных сообщений
async def handle_message(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f"Ты написал: {text}")

# Создаём и запускаем бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # Добавляем обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
