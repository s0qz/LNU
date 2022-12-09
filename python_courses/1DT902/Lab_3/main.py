import pycom
from machine import Pin
from dth import DTH
import socket
from time import sleep
from network import LoRa
import binascii
import struct

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868,
            adr=False, public=True, tx_retries=0)

print("DevEUI: " + binascii.hexlify(lora.mac()).decode('utf-8').upper())

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('4D125B4757233A4737809F680F5182C8')
dev_eui = binascii.unhexlify('70B3D54996506FC8')

auth = (dev_eui, app_eui, app_key)

lora.join(activation=LoRa.OTAA, auth=auth, timeout=0)

while not lora.has_joined():
    sleep(5)
    print('Not joined yet...')

print('Network joined!')

dht11 = DTH(Pin('P10', mode=Pin.OPEN_DRAIN), 0)
socket1 = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
socket1.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
socket1.setblocking(False)

while lora.has_joined():
    result = dht11.read()
    if result.is_valid():
        socket1.send(struct.pack('>h', int(result.temperature)) +
                     struct.pack('>h', int(result.humidity)))
        print('sent temperature:', result.temperature)
        print('sent humidity:', result.humidity)
    sleep(60)
