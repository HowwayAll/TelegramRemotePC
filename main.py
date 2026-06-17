
# Я КОММИТИЛ ЭТО ВСЁ НЕ С ТОЙ ПОЧТЫ

import telebot

from config import TOKEN
from utils.handlers import setup_handlers

bot = telebot.TeleBot(TOKEN)

setup_handlers(bot)

if __name__ == "__main__":
    bot.infinity_polling()