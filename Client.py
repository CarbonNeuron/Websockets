import websockets, asyncio
async def client():
    async with websockets.connect('ws://207.63.186.14:8080') as websocket:
        pass

asyncio.get_event_loop().run_until_complete(client())