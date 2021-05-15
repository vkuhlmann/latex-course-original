import uuid
import asyncio
import logging
import base64
import websockets
import json
import threading
import snippet
import time

loop = None
thr = None
isQuitRequested = False
sockets = set([])
interval = 0.5
heightRes = -1
measureTime = 10

def startSockets():
    global loop, thr

    loop = asyncio.new_event_loop()
    thr = threading.Thread(target=runSockets)
    thr.start()


def stopSockets():
    global isQuitRequested, thr, loop
    isQuitRequested = True

    if thr != None:
        thr.join()
    thr = None

    loop.call_soon_threadsafe(loop.stop)


def runSockets():
    asyncio.set_event_loop(loop)
    start_server = websockets.serve(socketListen, None, 6501)

    res = asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_until_complete(asyncio.wait([
        loop.create_task(doWebsocketSendloop())
    ]))

    if res != None:
        res.close()
        asyncio.get_event_loop().run_until_complete(res.wait_closed())

async def socketListen(websocket, path):
    #await register(websocket)
    try:
        sockets.add(websocket)
        async for message in websocket:
            await handleMessage(websocket, message)

    finally:
        sockets.remove(websocket)
        pass
        #await unregister(websocket)

def handleRequest(data):
    return None

async def handleMessage(websocket, message):
    return

    data = json.loads(message)
    ans = handleRequest(data)
    if ans != None:
        ans["type"] = "result"
        ans["correspondence"] = data["correspondence"]
        payload = json.dumps(ans)
        await websocket.send(payload)

async def doWebsocketSendloop():
    global heightRes

    measureStartTime = -1
    measureBandwidth = 0

    while not isQuitRequested:
        data = snippet.Snippet(heightRes)
        if heightRes < -1:
            heightRes = -1

        # print(f"Data length: {len(data)}")

        measureBandwidth += len(sockets) * len(data)
        if measureStartTime == -1:
            measureStartTime = time.time()
            measureBandwidth = 0

        elif measureTime > 0 and time.time() > measureStartTime + measureTime:
            rate = measureBandwidth / (time.time() - measureStartTime)
            print(f"Bandwidth: {rate * 8 / 1e6:.2f} Mbps")

            measureStartTime = time.time()
            measureBandwidth = 0

        if len(sockets) > 0:
            await asyncio.wait([
                loop.create_task(sock.send(data)) for sock in sockets])
        await asyncio.sleep(interval)

def main():
    global interval, heightRes, measureTime

    logFormat = "%(asctime)s: %(message)s"
    logging.basicConfig(format=logFormat, level=logging.INFO,
                        datefmt="%H:%M:%S")

    startSockets()

    print("Type 'quit' to stop")

    while True:
        cmd = input("> ")
        if cmd == "quit":
            break

        elif cmd == "snippet":
            snippet.Snippet()


        elif cmd.startswith("screen"):
            if cmd == "screen":
                print(f"Screen is {snippet.screen}")
            else:
                try:
                    i = int(cmd[len("screen "):])
                    snippet.setScreen(i)
                except Exception as ex:
                    print(f"Error setting value: {ex}")

        elif cmd.startswith("interval"):
            if cmd == "interval":
                print(f"Interval is {interval}")
            else:
                try:
                    newVal = float(cmd[len("interval "):])
                    interval = newVal
                except Exception as ex:
                    print(f"Error setting value: {ex}")


        elif cmd.startswith("height"):
            if cmd == "height":
                print(f"Height is {heightRes}")
            else:
                try:
                    newVal = int(cmd[len("height "):])
                    heightRes = newVal
                except Exception as ex:
                    print(f"Error setting value: {ex}")

        
        elif cmd.startswith("measuretime"):
            if cmd == "measuretime":
                print(f"Measuretime is {measureTime}")
            else:
                try:
                    newVal = float(cmd[len("measuretime "):])
                    measureTime = newVal
                except Exception as ex:
                    print(f"Error setting value: {ex}")

        else:
            print("Unknown command")
    
    stopSockets()

if __name__ == "__main__":
    main()
