import telebot

token = "telegram_bot_token"
admin_id = 1234567890
admin_username = "your_username"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    if message.from_user.username == admin_username and message.from_user.id == admin_id:
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
    else: pass
