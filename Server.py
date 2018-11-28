import websockets, asyncio
async def server(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")
startserver = websockets.serve(server, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(startserver)
asyncio.get_event_loop().run_forever()