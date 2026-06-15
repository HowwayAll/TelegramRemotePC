import telebot

import os
import pyautogui

token = "your_bot_token"

admin_id = 1234567890
admin_username = "username"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    if message.from_user.username == admin_username and message.from_user.id == admin_id:
        bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
    else: pass

@bot.message_handler(commands=["sleep", "s"])
def go_sleep(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            bot.send_message(message.chat.id, "<i>отправка ПК ко сну</i>", parse_mode="HTML")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            bot.send_message(message.chat.id, "<i>ПК проснулся</i>", parse_mode="HTML")
        else: pass

@bot.message_handler(commands=["poweroff", "po"])
def go_out(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            bot.send_message(message.chat.id, "<i>выключение ПК</i>", parse_mode="HTML")
            os.system("shutdown /s /t 0")
        else: pass

@bot.message_handler(commands=["force poweroff", "fpo"])
def force_out(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            bot.send_message(message.chat.id, "<i>принудительное выключение ПК</i>", parse_mode="HTML")
            os.system("shutdown /s /f /t 0")
        else: pass

@bot.message_handler(commands=["reboot", "r"])
def go_reboot(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            bot.send_message(message.chat.id, "<i>перезагрузка ПК</i>", parse_mode="HTML")
            os.system("shutdown /r /t 0")
        else: pass

@bot.message_handler(commands=["force reboot", "fr"])
def force_reboot(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            bot.send_message(message.chat.id, "<i>принудительная перезагрузка ПК</i>", parse_mode="HTML")
            os.system("shutdown /r /f /t 0")
        else: pass

@bot.message_handler(commands=['status'])
def send_status(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            bot.send_message(message.chat.id, "<i>Состояние ПК\n\nстатус: активен</i>", parse_mode="HTML")
        else: pass

@bot.message_handler(commands=["screenshot", "ss"])
def send_screenshot(message):
        if message.from_user.username == admin_username and message.from_user.id == admin_id:
            bot.send_message(message.chat.id, "<i>доступ разрешён</i>", parse_mode="HTML")
            screenshot = pyautogui.screenshot("image.png")
            bot.send_message(message.chat.id, "<i>изображение создано</i>", parse_mode="HTML")

            with open('image.png', 'rb') as image:
                bot.send_photo(message.chat.id, image)
            os.remove('image.png')
            bot.send_message(message.chat.id,"изображение удалено", parse_mode="HTML")
        else: pass
