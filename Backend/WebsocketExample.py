import asyncio
import pathlib
import ssl
import websockets
from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['192.168.0.103:9092'])
async def time(websocket, path):
    while True:
        for msg in consumer:
            message=str(msg.value)
            print(message)
            await websocket.send(message)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_cert_chain(localhost_pem)

start_server = websockets.serve(
    time, "127.0.0.1", 8765, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()