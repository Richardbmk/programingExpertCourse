# TIM SOLUTIONS
# Problem 02
import threading
from time import sleep
import math


def append_values(lst, values=[], delay=1):
    for value in values:
        lst.append(value)
        sleep(math.ceil(abs(delay)))


def append_integer(lst, integer):
    lst.append(integer)


lst = []

# Write your code here.

thread1 = threading.Thread(target=append_values, args=(lst, [1,3,5], 1))
thread2 = threading.Thread(target=append_integer, args=(lst, 4))
thread3 = threading.Thread(target=append_integer, args=(lst, 3))

# thread1.start()
# thread2.start()
# thread1.join()
# thread3.start()
# print(lst)

# Problem 03
# TIM SOLUTIONS
import threading
import math

RANGE_START = 0
RANGE_END = 1000

def is_power_of_two(x):
    if x == 0:
        return False
    # return type(math.log2(x)) is int --> log return a float number
    return (x & (x - 1)) == 0
    


powers_of_two = set()
set_lock = threading.Lock()

def find_powers_of_two(iter):
    for x in iter:
        if is_power_of_two(x):
            set_lock.acquire()
            powers_of_two.add(x)
            set_lock.release()

thread1 = threading.Thread(target=find_powers_of_two, args=(range(RANGE_START, 250),))
thread2 = threading.Thread(target=find_powers_of_two, args=(range(250, 500),))
thread3 = threading.Thread(target=find_powers_of_two, args=(range(500, 750),))
thread4 = threading.Thread(target=find_powers_of_two, args=(range(750, RANGE_END),))

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

# print(powers_of_two)


# Problem 04
# TIM SOLUTIONS
import threading

def print_foo(n, foo_lock, bar_lock):
    for _ in range(n):
        foo_lock.acquire()
        print("foo", end="")
        bar_lock.release()

def print_bar(n, foo_lock, bar_lock):
    for _ in range(n):
        bar_lock.acquire()
        print("bar", end="")
        foo_lock.release()


n = int(input("Enter a positive integer: "))

foo_lock = threading.Lock()
bar_lock = threading.Lock()
bar_lock.acquire()

foo_thread = threading.Thread(target=print_foo, args=(n, foo_lock, bar_lock))
bar_thread = threading.Thread(target=print_bar, args=(n, foo_lock, bar_lock))

foo_thread.start()
bar_thread.start()

foo_thread.join()
bar_thread.join()
