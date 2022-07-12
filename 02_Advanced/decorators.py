# Code Sample 00
# Welcome to our Python playground!
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time = end_time - start_time
        print(f"Time taken to execute: {total_time * 1000000} microseconds")
        return result

    return wrapper


def print_arguments(func):
    def wrapper(*args, **kwargs):
        print("Args:", args, "Kwargs:", kwargs)
        result = func(*args, **kwargs)
        return result

    return wrapper


def ignore_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Exception ignored:", e)
        return None

    return wrapper


@print_arguments
@ignore_exception
@timer
def loop(n):
    if n > 10000:
        raise Exception("n is too large to loop through!")
    for i in range(n):
        pass


# loop(12)
# loop(1000000)


# Sample code 01
def decorator(func):
    def wrapper(x):
        print("Wrapper function called func!", x)
        result = func()
        return result

    return wrapper


# def foo():
#     print("foo")

# foo = decorator(foo)
# foo(1)

@decorator
def foo():
    print("foo")

# foo(1)

# Sample code 02
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper function called func!")
        result = func(*args, **kwargs)
        return result

    return wrapper

@decorator
def foo(x, y, z=None):
    print(x, y, z)

# foo(2, 3)

# Sample Code 03
import time 

def timers(func):
    def wrappers(*args, **kwargs):
        start_time = time.time()
        result = func(*args, kwargs)
        end_time = time.time

        total_time = end_time - start_time
        print("Time taken to execute:", total_time)
        return result

    return wrappers

def pretty_printer(func):
    def wrapper(*args, **kwargs):
        print("---")
        result = func(*args, **kwargs)
        print("---")
        return result

    return wrapper

@timer
def loops():
    for _ in range(100000):
        pass

# loops()

@timer
def get_max(x,y,z):
    loops()
    return max(x,y,z)

# print(get_max(1,2,3))

@timer
@pretty_printer
def print_numbers(num):
    for i in range(num):
        print(i)

print_numbers(100)