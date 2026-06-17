from functools import wraps

def access_checker(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        from config import TELEGRAM_ID
        if message.from_user.id == TELEGRAM_ID:
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