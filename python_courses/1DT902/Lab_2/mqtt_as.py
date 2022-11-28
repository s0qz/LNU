from time import sleep
from mqtt_async import MQTTClient, config
import uasyncio as asyncio


class MQTTConnect:
    def mqtt_connect():
        config['server'] = '64.225.110.253'
        config['port'] = '1883'
        config['user'] = 'king'
        config['password'] = 'arthur'
        config['ssid'] = 'Anonymous'
        config['wifi_pw'] = '3q1t6ibj'

        async def messages(client):  # Respond to incoming messages
            async for topic, msg, retained in client.queue:
                print((topic, msg, retained))

        async def up(client):  # Respond to connectivity being (re)established
            while True:
                await client.up.wait()  # Wait on an Event
                client.up.clear()
                await client.subscribe('test/dev', 1)  # renew subscriptions

        async def main(client):
            await client.connect()
            for coroutine in (up, messages):
                asyncio.create_task(coroutine(client))
            n = 0
            while True:
                await asyncio.sleep(5)
                print('publish', n)
                # If WiFi is down the following will pause for the duration.
                await client.publish('result', '{}'.format(n), qos=1)
                n += 1

        config["queue_len"] = 1  # Use event interface with default queue size
        MQTTClient.DEBUG = True  # Optional: print diagnostic messages
        client = MQTTClient(config)
        try:
            asyncio.run(main(client))
        finally:
            client.disconnect()
