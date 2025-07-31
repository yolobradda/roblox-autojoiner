import asyncio
import threading
import keyboard

import websockets
from websockets import WebSocketServerProtocol
from config import WEBSOCKET_PORT
from src.logger.logger import setup_logger
from src.utils import set_console_title

logger = setup_logger()
connected_clients = set()
paused = False


async def handler(websocket: WebSocketServerProtocol):
    logger.info(f"> New client: {websocket.remote_address}")
    connected_clients.add(websocket)

    try:
        await asyncio.Future()
    finally:
        connected_clients.remove(websocket)


async def broadcast(message: str):
    if paused:
        return

    dead_clients = set()

    for client in connected_clients:
        try:
            await client.send(message)
        except websockets.ConnectionClosed:
            dead_clients.add(client)

    if dead_clients:
        connected_clients.difference_update(dead_clients)

    #logger.info(f"Отправил скрипт для входа {len(connected_clients)} клиентам") # флудит сильно


async def main():
    async with websockets.serve(handler, "127.0.0.1", WEBSOCKET_PORT):
        logger.info(f"> Websocket server started: ws://127.0.0.1:{WEBSOCKET_PORT}")
        await asyncio.Future()


def toggle_pause():
    global paused
    paused = not paused

    status_text = "Pause" if paused else "Enabled"
    logger.info(
        "> The script is paused (messages are parsed but not sent to the rblx)"
        if paused else "> The script continued to run."
    )

    set_console_title(f"AutoJoiner | Status: {status_text}")

def keybrd_listener():
    keyboard.add_hotkey('F2', toggle_pause)
    keyboard.wait()


def roblox_main():
    threading.Thread(target=keybrd_listener, daemon=True).start()
    asyncio.run(main())

# https://github.com/notasnek/roblox-autojoiner