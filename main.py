import asyncio
import threading
from discord import listener
from src.roblox import roblox_main
from src.utils import set_console_title
import time

# https://github.com/notasnek/roblox-autojoiner
# буду рад звезде на репозитории / please STAR my repo

if __name__ == "__main__":
    set_console_title(f"AutoJoiner | Status: Enabled")

    print("Starting in 3 seconds...")
    time.sleep(3)

    threading.Thread(target=roblox_main, daemon=True).start()
    asyncio.run(listener())
