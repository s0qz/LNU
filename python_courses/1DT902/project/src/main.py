from machine import Pin
from time import sleep
from dht import DHT11

dht11 = DHT11(Pin(0))

while True:
    dht11.measure()
    print(f"Temprature: {dht11.temperature()} °C and Humidity: {dht11.humidity()} %")
    sleep(300)
