import asyncio
import websockets
import json

async def connect_and_send_message(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"message": message}))

        while True:
            try:
                response = await websocket.recv()
                data = json.loads(response)
                if data["type"] == "stream":
                    print(f"Streamed echo: {data['data']}")
                elif data["type"] == "stream_reverse":
                    print(f"Streamed reverse echo: {data['data']}")
                elif data["type"] == "count":
                    print(f"Last char '{data['last_char']}' count: {data['count']}")
            except websockets.ConnectionClosed:
                print("Connection closed")
                break

message = "The quick brown fox jumped over the lazy dog o"
uri = "ws://localhost:8765"

asyncio.get_event_loop().run_until_complete(connect_and_send_message(uri, message))