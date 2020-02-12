import asyncio
import datetime
import random
import websockets
import time
i=0
async def times(websocket, path):
    while True:
        now = "some-values"
        await websocket.send(now)
        time.sleep(1)

start_server = websockets.serve(times, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
