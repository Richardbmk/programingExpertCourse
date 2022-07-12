def add_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result += 1
        return result 

    return wrapper

@add_one
def add_values(x, y):
    return x + y

print(add_values(-5,100))


# TIM Solution
def add_one(func):
    def wrapper(x, y):
        return_value = func(x, y)
        return return_value + 1

    return wrapper


@add_one
def add_values(x, y):
    return x + y