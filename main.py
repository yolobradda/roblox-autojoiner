import asyncio
import threading
import time

from discord import listener
from src.roblox import roblox_main


# https://github.com/notasnek/roblox-autojoiner
# буду рад звезде на репозитории / please STAR my repo


if __name__ == "__main__":
    print("Roblox AutoJoiner for Chilli's Notify by jvrre")
    print("Github: https://github.com/notasnek/roblox-autojoiner")
    print("Join our discord: https://discord.gg/fQSP3VFks9")

    print()
    print("Hey! Wait! You can help me for free...")
    print("Just click on this link to view the ad at least twice a day (to receive or renew your key)")
    print("https://ads.luarmor.net/get_key?for=Key_for_AutoJoiner-XqMcbHPoLXoL")
    print("You can also donate to me on Discord. Thank you!")
    print()

    print("Version: 1.1.1")
    print("Starting in 5 seconds...")
    print()

    # убирая мое авторство вы нарушаете лицензию (читай LICENSE.md)
    # By removing my authorship, you are violating the license (read LICENSE.md)
    # notasnek

    time.sleep(5)

    threading.Thread(target=roblox_main, daemon=True).start()
    asyncio.run(listener())



# https://github.com/notasnek/roblox-autojoiner
