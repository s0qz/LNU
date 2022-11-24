from machine import Pin
import time
import _thread


def main():
    print("Hello pico")


_thread.start_new_thread(main, ())

count = 0

while count < 10:
    p8 = Pin(15, Pin.OUT)
    p9 = Pin(14, Pin.OUT)
    p10 = Pin(13, Pin.OUT)
    p8.value(1)
    time.sleep(1)
    p8.value(0)
    p9.value(1)
    time.sleep(1)
    p9.value(0)
    p10.value(1)
    time.sleep(1)
    p10.value(0)
    count += 1
