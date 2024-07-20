import asyncio
import websockets
import json

async def stream_message(websocket, message):
    for char in message:
        await websocket.send(json.dumps({"type": "stream", "data": char}))
        await asyncio.sleep(0.1)

async def stream_reverse_message(websocket, message):
    for char in reversed(message):
        await websocket.send(json.dumps({"type": "stream_reverse", "data": char}))
        await asyncio.sleep(0.1)

async def count_last_char(websocket, message):
    if message:
        last_char = message[-1]
        count = message[:-1].count(last_char)
        await websocket.send(json.dumps({"type": "count", "last_char": last_char, "count": count}))

async def handler(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        text = data.get("message", "")
        
        await stream_message(websocket, text)
        await stream_reverse_message(websocket, text)
        await count_last_char(websocket, text)

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()