from functools import wraps

def access_checker(bot):
    def decorator(func):
        @wraps(func)
        def wrapper(message, *args, **kwargs):
            from config import TELEGRAM_ID
            if message.from_user.id == TELEGRAM_ID:
                bot.send_message(message.chat.id, "<i>Доступ разрешён</i>", parse_mode="HTML")
                return func(message, *args, **kwargs)
            else:
                bot.send_message(message.chat.id, "<i>Неизвестная команда</i>", parse_mode="HTML")
                return None
        return wrapper