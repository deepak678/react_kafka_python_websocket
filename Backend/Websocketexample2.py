import asyncio
import datetime
import random
import websockets
from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['192.168.0.103:9092'])

async def time(websocket, path):
    while True:
        for msg in consumer:
            message=str(msg.value)
            print(message)
            await websocket.send(message)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
