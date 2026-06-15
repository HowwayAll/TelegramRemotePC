import telebot

import os
import pyautogui
import keyboard

from functools import wraps

token = "your_bot_token"
admin_id = 1234567890
admin_username = "username"

bot = telebot.TeleBot(token)

LANGS = {
    "ru": {
          "granted": "<i>доступ разрешён</i>",
          "sleep": "<i>отправка ПК ко сну</i>",
          "wakeup": "<i>ПК снова активен</i>",
          "turnoff": "<i>выключение ПК</i>",
          "reboot": "<i>перезагрузка ПК</i>",
          "image_created": "<i>изображение создано</i>",
          "image_delted": "<i>изображение удалено</i>"
    },
    "en": {
          "granted": "<i>access granted</i>",
          "sleep": "<i>sending PC to sleep</i>",
          "wakeup": "<i>PC is activated again</i>",
          "turnoff": "<i>turning off PC</i>",
          "reboot": "<i>rebooting PC</i>",
          "image_created": "<i>image created</i>",
          "image_delted": "<i>image deleted</i>"    
    }
}

def access_checker(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        if message.from_user.id == admin_id:
            return func(message, *args, **kwargs)
        else:
            return None
    return wrapper

def get_text(message, key):
     user_lang = message.from_user.language_code
     lang_pack = LANGS.get(user_lang, LANGS['en'])
     return lang_pack.get(key, "Error: missing text")




@bot.message_handler(commands=["start"])
@access_checker
def send_welcome(message):
    text = get_text(message, "granted")
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(commands=["sleep", "s"])
@access_checker
def go_sleep(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        text = get_text(message, "sleep")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        text = get_text(message, "wakeup")
        bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(commands=["poweroff", "po"])
@access_checker
def go_out(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        text = get_text(message, "turnoff")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        os.system("shutdown /s /t 0")

@bot.message_handler(commands=["reboot", "r"])
@access_checker
def go_reboot(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        text = get_text(message, "reboot")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        os.system("shutdown /r /t 0")

@bot.message_handler(commands=["screenshot", "ss"])
@access_checker
def send_screenshot(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        screenshot = pyautogui.screenshot("image.png")
        text = get_text(message, "image_created")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        with open('image.png', 'rb') as image:
            bot.send_photo(message.chat.id, image)
        os.remove('image.png')
        text = get_text(message, "image_deleted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(commands=["t"])
@access_checker
def type_it(message):
    text = message.text
    text = text.removeprefix("/t ")
    keyboard.write(text)

bot.infinity_polling()
