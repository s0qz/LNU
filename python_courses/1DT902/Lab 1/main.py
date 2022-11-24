from machine import Pin
from picozero import Speaker, TemperatureSensor
from time import sleep, time
from math import log, pow
import dht
import _thread


def temp_conversion(voltage):
    A = 0.001129148
    B = 0.000234125
    C = 0.0000000876741
    R = (voltage * 10000) / (3.3 - voltage)
    B_log = B * log(R)
    R_log = log(R)
    C_pow = C * pow(R_log, 3)
    return (1 / (A + B_log + C_pow)) - 273.15


def mario_song():
    global mario
    global buzzer
    for note in mario:
        if note < 2000:
            led_r.on()
        elif note < 3000:
            led_y.on()
        else:
            led_g.on()

        buzzer.play(note, 0.15)
        led_r.off()
        led_y.off()
        led_g.off()
    buzzer.off()


def temperature():
    d.measure()
    print(f"Temprature: {round(analog_temp.temp)} °C")
    print(f"Temprature: {d.temperature()} °C and Humidity: {d.humidity()} %")


def main():
    global start
    global time_diff
    global count

    while time_diff < 60:
        time_diff = time() - start
        if button.value() and time_diff >= 1:
            count += 1
            print(
                f"Button was pressed: {count} time(s). Time since last {time_diff}ms")
            play = True
            start = time()
        elif button.value() and time_diff < 1:
            print(
                f"Ignored button press: Time left for next press is {1 - time_diff}ms")


button = Pin(0, Pin.IN)

buzzer = Speaker(1)

analog_temp = TemperatureSensor(28, conversion=temp_conversion)

d = dht.DHT11(Pin(27))

led_r = Pin(15, Pin.OUT)
led_y = Pin(14, Pin.OUT)
led_g = Pin(13, Pin.OUT)

play = False
start = 0
time_diff = 0
count = 0

E7 = 2637
F7 = 2794
C7 = 2093
G7 = 3136
G6 = 1568
E6 = 1319
A6 = 1760
B6 = 1976
AS6 = 1865
A7 = 3520
D7 = 2349

mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6,
         0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7,
         G7, 0, E7, 0, C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0,
         B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0, C7, D7, B6,
         0, 0]

_thread.start_new_thread(main, ())

start = time()

while True:
    sleep(0.05)
    temperature()
    if play:
        mario_song()
        sleep(0.15)
