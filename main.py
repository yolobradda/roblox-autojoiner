import asyncio
import threading
from discord import listener
from src.roblox import roblox_main
from src.utils import set_console_title

# https://github.com/notasnek/roblox-autojoiner
# буду рад звезде на репозитории
# please STAR my repo

if __name__ == "__main__":
    set_console_title(f"AutoJoiner | Status: Enabled")

    print("Press ENTER to continue.")
    input("Have you configured the `config.py` file?")
    input("Did you move the `joiner.lua` file from the `data` folder to the `AutoExec` folder of your executor?")

    threading.Thread(target=roblox_main, daemon=True).start()
    asyncio.run(listener())
