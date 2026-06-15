import telebot

import os
import pyautogui
import keyboard

from functools import wraps

token = "your_bot_token"
admin_id = 1234567890
admin_username = "username"

bot = telebot.TeleBot(token)



def access_checker(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        if message.from_user.id == admin_id:
            return func(message, *args, **kwargs)
        else:
            return None



@bot.message_handler(commands=["start"])
@access_checker
def send_welcome(message):
    bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")

@bot.message_handler(commands=["sleep", "s"])
@access_checker
def go_sleep(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        bot.send_message(message.chat.id, "<i>отправка ПК ко сну</i>", parse_mode="HTML")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        bot.send_message(message.chat.id, "<i>ПК проснулся</i>", parse_mode="HTML")

@bot.message_handler(commands=["poweroff", "po"])
@access_checker
def go_out(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        bot.send_message(message.chat.id, "<i>выключение ПК</i>", parse_mode="HTML")
        os.system("shutdown /s /t 0")

@bot.message_handler(commands=["force poweroff", "fpo"])
@access_checker
def force_out(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        bot.send_message(message.chat.id, "<i>принудительное выключение ПК</i>", parse_mode="HTML")
        os.system("shutdown /s /f /t 0")

@bot.message_handler(commands=["reboot", "r"])
@access_checker
def go_reboot(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        bot.send_message(message.chat.id, "<i>перезагрузка ПК</i>", parse_mode="HTML")
        os.system("shutdown /r /t 0")

@bot.message_handler(commands=["force reboot", "fr"])
@access_checker
def force_reboot(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        bot.send_message(message.chat.id, "<i>принудительная перезагрузка ПК</i>", parse_mode="HTML")
        os.system("shutdown /r /f /t 0")

@bot.message_handler(commands=['status'])
@access_checker
def send_status(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        bot.send_message(message.chat.id, "<i>Состояние ПК\n\nстатус: активен</i>", parse_mode="HTML")

@bot.message_handler(commands=["screenshot", "ss"])
@access_checker
def send_screenshot(message):
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
        screenshot = pyautogui.screenshot("image.png")
        bot.send_message(message.chat.id, "<i>изображение создано</i>", parse_mode="HTML")
        with open('image.png', 'rb') as image:
            bot.send_photo(message.chat.id, image)
        os.remove('image.png')
        bot.send_message(message.chat.id,"изображение удалено", parse_mode="HTML")

@bot.message_handler(commands=["t"])
@access_checker
def type_it(message):
    text = message.text
    text = text.removeprefix("/t ")
    keyboard.write(text)

bot.infinity_polling()
