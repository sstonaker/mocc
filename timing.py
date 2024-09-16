from datetime import datetime


def time_function(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        f = func(*args, **kwargs)
        end = datetime.now()
        print(f"Ran in {end-start} seconds.")
        return f
    return wrapper