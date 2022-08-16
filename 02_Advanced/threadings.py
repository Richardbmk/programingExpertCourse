# Sample 00
# Welcome to our Python playground!

import random
import time
import threading


def loop(thread_name, n):
    for i in range(n):
        # Sleep for up to 20 milliseconds.
        time.sleep(random.randint(1, 20) / 1000)
        print(f"Thread {thread_name}: {i}")


# TODO: As an exercise, try to change this code to let
# t1 finish first before t2 starts running. (Hint: A
# mutex lock should do the trick)
t1 = threading.Thread(target=loop, args=("t1", 10))
t2 = threading.Thread(target=loop, args=("t2", 10))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Sample code 01
import threading
from time import sleep

def run(content, delay=1):
    sleep(delay)
    print(content)

thread1 = threading.Thread(target=run, args=("run 1", 1))
thread2 = threading.Thread(target=run, args=("run 2", 1))

# thread1.start()
# # print("main thread")
# # thread1.join()
# thread2.start()

# print(threading.active_count())

# thread1.join()
# thread2.join()
# print("done!")

# Sample code 02
import threading 
from time import sleep

def print_values(values, delay):
    for item in values:
        print(item)
        sleep(delay)

thread1 = threading.Thread(target=print_values, args=([1,3,5], 0.2))
thread2 = threading.Thread(target=print_values, args=([2,4], 0.3))

# thread1.start()
# thread2.start()

# Sample code 03
from threading import Lock, Thread
from time import sleep

# mutex = Lock()
# mutex.acquire()
# mutex.release()

def t1(lock):
    print("starting t1")
    lock.acquire()
    sleep(1)
    print("t1")
    lock.release()

def t2(lock):
    print("starting t2")
    lock.acquire()
    sleep(1)
    print("t2")
    lock.release()

lock = Lock()
thread1 = Thread(target=t1, args=(lock, ))
thread2 = Thread(target=t2, args=(lock, ))

# thread1.start()
# thread2.start()

# Sample code 04
from threading import Lock, Thread
from time import sleep

def print_values(values, start_lock, end_lock, name):
    for item in values:
        print(f"{name} waiting for lock")
        start_lock.acquire()
        print(item)
        end_lock.release()

lock1 = Lock()
lock2 = Lock()
lock2.acquire()

thread1 = Thread(target=print_values, args=([1,3,5], lock1, lock2, "t1"))
thread2 = Thread(target=print_values, args=([2,4], lock2, lock1, "t2"))

# thread1.start()
# thread2.start()

# Sample code 05
from threading import Lock, Thread
from time import sleep

def start_game(preq=[]):
    print("Waiting to start game.")

    for t in preq:
        t.join()

    print("Started game!")

def load_assets():
    sleep(2)
    print("loaded assets")

def load_player():
    sleep(1)
    print("loaded player")

load_assets_thread = Thread(target=load_assets)
load_player_thread = Thread(target=load_player)
preq = [load_player_thread, load_assets_thread]

start_game_thread = Thread(target=start_game, args=(preq,))


# load_assets_thread.start()
# load_player_thread.start()

# start_game_thread.start()

# Sample Code 05
from threading import Thread, Lock
from time import sleep

def wait_on_threads(thread):
    for thread in threads:
        thread.join()

    print("ran")

threads = []

t1 = Thread(target=wait_on_threads, args=(threads,))
t2 = Thread(target=wait_on_threads, args=([t1],))
# threads.append(t2)

# t1.start()
# t2.start()