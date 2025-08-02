
# https://github.com/notasnek/roblox-autojoiner



DISCORD_TOKEN = "your discord token" # discord token / дискорд токен
# гайд/guide: https://www.youtube.com/results?search_query=how+to+get+discord+token

MONEY_THRESHOLD = 10.0 # in millions / в миллионах (example: 1.5 = 1.5m, 0.5 = 500k)
# if the brainrot is less than this number, it will be skipped
# если заработок в секунду у брейнрота меньше этого числа, он будет скипнут

PLAYER_TRESHOLD = 8 # число / number
# if there are more PLAYER_TRESHOLD players on the server - it will not try to enter the server
# если на сервере больше PLAYER_TRESHOLD игроков - не будет пытаться зайти на сервер

IGNORE_UNKNOWN = True # True / False
# ignore "Unknown" brainrots
# игнорировать "Unknown" брейнротов

BYPASS_10M = True # True / False
# bypass jobid for 10m+ servers, FOR WORKING BYPASS YOU MUST HAVE INJECTED CHILLI HUB
# байпасить вход для 10м+ серваков, ДЛЯ РАБОЧЕГО БУПАССА У ВАС ДОЛЖЕН БЫТЬ ЗАИНЖЕКЧЕН ЧИЛЛИ ХАБ



# don't touch it if you don't understand what it is / не трогай если не понимаешь что это
WEBSOCKET_PORT = 51948 # websocket port for data transfer in roblox

DISCORD_WS_URL = "wss://gateway.discord.gg/?v=10&encoding-json" # discord ws

CHILLI_HUB_CHANNELS_ID = {
    "under_500k": ["1394958052536619059", "1400301860178628739"], # under 500k channels
    "500k_1m": ["1394958062166474823", "1400302142702751864"], # 500k - 1M channels
    "1m-10m": ["1394958060828627064", "1400302392431349770"], # 1m - 10m channels
    "10m_plus": ["1394958063341015081"] # 10m+ channels
}



# https://github.com/notasnek/roblox-autojoiner