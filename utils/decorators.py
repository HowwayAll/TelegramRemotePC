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
    return decorator

def get_errors(bot):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                message = next((arg for arg in args if hasattr(arg, 'chat')), None)
                if message:
                    bot.send_message(message.chat.id, f"<i>Непредвиденная ошибка: {error}</i>", parse_mode="HTML")
        return wrapper
    return decorator