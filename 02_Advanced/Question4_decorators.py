def print_return_value(func):
    def  wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper

# TIM Solution
def print_return_value(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        print(return_value)
        return return_value

    return wrapper

