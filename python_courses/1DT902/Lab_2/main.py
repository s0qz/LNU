from Lab_2.internet import Internet
from Lab_2.mqtt import MQTTConnect
from machine import Pin
from picozero import Speaker
from time import sleep, time


button = Pin(0, Pin.IN)

buzzer = Speaker(1)

note = 2300

car_r = Pin(15, Pin.OUT)
car_y = Pin(14, Pin.OUT)
car_g = Pin(13, Pin.OUT)
pedestrian_r = Pin(16, Pin.OUT)
pedestrian_y = Pin(17, Pin.OUT)
pedestrian_g = Pin(18, Pin.OUT)


def traffic_go():
    car_r.off()
    car_y.off()
    car_g.on()
    pedestrian_r.on()
    pedestrian_g.off()


def traffic_soon_stop():
    car_g.off()
    car_y.on()
    sleep(2)
    all_stop()


def all_stop():
    car_r.on()
    car_y.off()
    sleep(1)
    pedestrian_go()


def pedestrian_go():
    pedestrian_r.off()
    pedestrian_y.off()
    pedestrian_g.on()
    start_pedestrian_go = time()
    now = 0
    while now - start_pedestrian_go < 3:
        buzzer.play(note, 0.25, 5)
        buzzer.play(note, 0.1, 0)
        now = time()
    pedestrian_soon_stop()


def pedestrian_soon_stop():
    pedestrian_r.off()
    pedestrian_g.on()
    start_pedestrian_soon_stop = time()
    now = 0
    while now - start_pedestrian_soon_stop < 1:
        buzzer.play(1000, 0.4, 5)
        buzzer.play(1000, 0.2, 0)
        now = time()
    traffic_get_ready()


def traffic_get_ready():
    car_y.on()
    pedestrian_r.on()
    pedestrian_g.off()
    sleep(1)
    traffic_go()


def buttonEventCallback():
    pedestrian_y.on()
    sleep(4)
    traffic_soon_stop()


# Internet.connect()
MQTTConnect.mqtt_connect()

while True:
    traffic_go()
    if button.value():
        buzzer.play(note, 0.5, 5)
        buttonEventCallback()
