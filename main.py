
# добавить /resources которая отправляет загруженность ЦП / ВИДЕОКАРТЫ / ОЗУ / и другое...
# добавить /volume [0-100] для управления звуком PYCAWD
# добавить логирование

import telebot

import os
import pyautogui
import keyboard

from functools import wraps

from config import TELEGRAM_ID
from config import TOKEN

token = TOKEN
admin_id = TELEGRAM_ID

bot = telebot.TeleBot(token)

LANGS = {
    "ru": {
          "granted": "<i>доступ разрешён</i>",
          "sleep": "<i>отправка ПК ко сну</i>",
          "wakeup": "<i>ПК снова активен</i>",
          "turnoff": "<i>выключение ПК</i>",
          "reboot": "<i>перезагрузка ПК</i>",
          "image_created": "<i>изображение создано</i>",
          "image_deleted": "<i>изображение удалено</i>"
    },
    "en": {
          "granted": "<i>access granted</i>",
          "sleep": "<i>sending PC to sleep</i>",
          "wakeup": "<i>PC is activated again</i>",
          "turnoff": "<i>turning off PC</i>",
          "reboot": "<i>rebooting PC</i>",
          "image_created": "<i>image created</i>",
          "image_deleted": "<i>image deleted</i>"    
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

def error_catcher(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        try:
            return func(message, *args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            return None
    return wrapper

def logger(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        user = message.from_user
        print(f"User {user.id} ({user.username}) called {func.__name__} with args: {args} kwargs: {kwargs}")
        return func(message, *args, **kwargs)
    return wrapper

def get_text(message, key):
     user_lang = message.from_user.language_code
     lang_pack = LANGS.get(user_lang, LANGS['en'])
     return lang_pack.get(key, "Error: missing text / check dictionary")




@bot.message_handler(commands=["start"])
@access_checker
def send_welcome(message):
    text = get_text(message, "granted")
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(commands=["sleep", "s"])
@access_checker
@error_catcher
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
@error_catcher
def go_out(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        text = get_text(message, "turnoff")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        os.system("shutdown /s /t 0")

@bot.message_handler(commands=["reboot", "r"])
@access_checker
@error_catcher
def go_reboot(message):
        text = get_text(message, "granted")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        text = get_text(message, "reboot")
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        os.system("shutdown /r /t 0")

@bot.message_handler(commands=["screenshot", "ss"])
@access_checker
@error_catcher
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
@error_catcher
def type_it(message):
    text = message.text
    text = text.removeprefix("/t")
    if text == "":
        return None
    else:
        text = text.removeprefix(" ")
        keyboard.write(text)


@bot.message_handler(commands=["kill"])
@access_checker
@error_catcher
def kill_task(message):
    text = message.text
    text = text.removeprefix("/kill")
    if text == "":
        return None
    else:
        text = text.removeprefix(" ")
        os.system(f"taskkill /f /im {text}")



if __name__ == "__main__":
    bot.infinity_polling()