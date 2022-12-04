import uasyncio as asyncio
from machine import Pin
from picozero import Speaker
from time import sleep, time
from Lab_2.mqtt_as import MQTTClient, config

ped_leds = {
    'YELLOW': Pin(17, Pin.OUT),
    'GREEN': Pin(18, Pin.OUT),
    'RED': Pin(16, Pin.OUT),
}

buzzer = Speaker(1)
note = 2400

button = Pin(0, Pin.IN)

REMOTE_DIR = 'SL'
OTHER_PI = 'l_status'
MY_PY = 's_status'

# MQTT STUFF
config['ssid'] = 'Anonymous'
config['wifi_pw'] = '3q1t6ibj'
config['server'] = 'mqtt.iotlab.dev'
config['port'] = 1883
config['user'] = 'king'
config['password'] = 'arthur'
MQTTClient.DEBUG = True

peds_lights = 0


def callback(topic, msg, retained):
    decoded = msg.decode('utf-8')
    print((topic, decoded, retained))

    if decoded == 'GREEN' or decoded == 'YELLOW':
        pass
    elif decoded == 'RED':
        sleep(1)
        go()
    else:
        print(f'unrecognised message "{decoded}"')


def go():
    global peds_lights
    peds_lights = 2
    for led in ped_leds.values():
        led.off()
    ped_leds['GREEN'].on()
    client.publish(REMOTE_DIR + '/' + MY_PY, 'GREEN', qos=1)
    start_pedestrian_go = time()
    now = 0
    while now - start_pedestrian_go < 3:
        buzzer.play(note, 0.25, 5)
        buzzer.play(note, 0.1, 0)
        now = time()
    stop()


def stop():
    global peds_lights
    start_pedestrian_soon_stop = time()
    now = 0
    n = 0
    if n != 0:
        while now - start_pedestrian_soon_stop < 1:
            buzzer.play(1000, 0.4, 5)
            buzzer.play(1000, 0.2, 0)
            now = time()
    n += 1
    peds_lights = 0
    ped_leds['GREEN'].off()
    ped_leds['RED'].on()


def buttonEventCallback():
    global peds_lights
    ped_leds['YELLOW'].on()
    peds_lights = 1


async def conn_han(client):
    await client.subscribe(REMOTE_DIR + '/' + OTHER_PI, 1)


async def main(client):
    global peds_lights
    await client.connect()
    for led in ped_leds.values():
        led.off()
    ped_leds['RED'].on()
    lights_msg = ''
    stop()

    while True:
        if peds_lights == 0:
            lights_msg = 'RED'
        elif peds_lights == 1:
            lights_msg = 'YELLOW'
        elif peds_lights == 2:
            lights_msg = 'GREEN'
        print(peds_lights, lights_msg)
        await client.publish(REMOTE_DIR + '/' + MY_PY, lights_msg, qos=1)
        if button.value():
            buzzer.play(note, 0.5, 5)
            buttonEventCallback()

config['subs_cb'] = callback
config['connect_coro'] = conn_han
client = MQTTClient(config)

try:
    asyncio.run(main(client))
finally:
    client.disconnect()
