import asyncio
import websockets


async def server(websocket, path):
    pass

start_server = websockets.serve(server, '207.63.186.14', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()