from machine import Pin
from time import sleep
import dht

dht11 = dht.DHT11(Pin(0))

while True:
    dht11.measure()
    print(f"Temprature: {d.temperature()} °C and Humidity: {d.humidity()} %")
    sleep(300)
