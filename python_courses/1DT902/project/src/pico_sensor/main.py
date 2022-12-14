from umachine import Pin, ADC
from time import sleep
from dht import DHT11
import urequests as requests
import network

dht11 = DHT11(Pin(0))

ky028 = ADC(Pin(28))


def read_temp():
    return ky028.read_u16() * (3.3 / 4095) * 2


def connect():
    ssid = 'LNU-iot'
    password = 'modermodemet'

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('Waiting for connection...')
        sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('Connection Failed')
    else:
        print('Connected to WiFi')
        status = wlan.ifconfig()
        print('ip = ' + status[0])


connect()

while True:
    dht11.measure()
    temperature_ky = read_temp()
    temp = round((dht11.temperature() + temperature_ky) / 2, 1)
    humid = dht11.humidity()
    print(
        f"Temprature: {temp} °C and Humidity: {humid} %")

    req = requests.post('http://billenius.com:8579', headers={
        'x-celsius': str(temp),
        'x-humidity': str(humid),
        'x-password': 'JA4eRQhwizvMB69VA2UgXu5iP9KsgatvsCxnExjyBy3em',
    }).content
    sleep(300)
