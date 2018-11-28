import websockets, asyncio
async def server(websocket, path):
    pass
startserver = websockets.serve(server, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(startserver)
asyncio.get_event_loop().run_forever()