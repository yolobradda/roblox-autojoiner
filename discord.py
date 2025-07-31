import asyncio
import websockets
import websockets.exceptions
import json
from src.logger.logger import setup_logger

from config import DISCORD_WS_URL, DISCORD_TOKEN, MONEY_THRESHOLD
from src.roblox import broadcast
from src.utils import check_channel, extract_server_info
logger = setup_logger()
enabled = False

async def identify(ws):
    identify_payload = {
        "op": 2,
        "d": {
            "token": DISCORD_TOKEN,
            "properties": {
                "os": "Windows", "browser": "Chrome", "device": "", "system_locale": "ru-RU",
                "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
                "referrer": "https://discord.com/", "referring_domain": "discord.com"
            }
        }
    }

    await ws.send(json.dumps(identify_payload))
    logger.info("Sent client identification")


async def heartbeat(ws, interval, last_sequence):
    await asyncio.sleep(interval)
    #await ws.send(json.dumps({"op": "2", "d": "null", "s": last_sequence}))
    #logger.info("Отправил heartbeat")
    # delete
    # не нужная функция прилетает `received 4001 (private use) Unknown opcode.; then sent 4001 (private use) Unknown opcode`


async def message_check(event):
    global enabled

    channel_id = event['d']['channel_id']
    result, category = check_channel(channel_id)
    if result:
        parsed = extract_server_info(event)
        if not parsed: return

        if parsed['money'] >= MONEY_THRESHOLD:
            if not enabled:
                logger.info("Caught the first message, starting my work") # на самом деле безполезная дичь
                enabled = True

            logger.info(f"+ New message in category {category}: {parsed['money']} m/sec / {parsed['name']}")
            await broadcast(parsed['script'])


async def message_listener(ws):
    last_sequence = None
    while True:
        event = json.loads(await ws.recv())
        #logger.info(f"Получил ивент: {str(event)[:2000]}")
        op_code = event.get("op", None)

        if op_code == 10: # Hello
            interval = event["d"]["heartbeat_interval"] / 1000
            asyncio.create_task(heartbeat(ws, interval, last_sequence))

        elif op_code == 0: # Dispatch
            last_sequence = event.get("s", None)
            event_type = event.get("t")

            if event_type == "MESSAGE_CREATE":
                await message_check(event)

        elif op_code == 9: # Invalid Session
            logger.warning("The session has ended, creating a new one..")
            await identify(ws)



async def listener():
    while True:
        try:
            async with websockets.connect(DISCORD_WS_URL, max_size=None) as ws:
                await identify(ws)
                await message_listener(ws)

        except websockets.exceptions.ConnectionClosed as e:
            logger.error(f" - WebSocket closed with error: {e}. Trying to reconnect...")
            await asyncio.sleep(5)
            continue

# https://github.com/notasnek/roblox-autojoiner