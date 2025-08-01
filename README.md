# Roblox AutoJoiner for Chilli Notify's (Steal a Brainrot)

A script for automatically connecting to servers in Roblox, from logs in Chilli Hub (Steal A Brainrot game). Allows you to filter by the amount of “earnings per second” on Brainrot and automatically connect to the server.

Скрипт для автоматического подключения к серверам в Roblox из логов в Chilli Hub (плейс Steal A Brainrot). Позволяет фильтровать по количеству "заработка в секунду" у брейнрота и автоматически подключаться к серверу.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](data/screenshot.png)

## ⚙️ Capabilities
- Earnings filtering - does not connect to servers if brainrot's earnings per second are below the specified threshold.

- Discord integration - uses a Discord token to listen to notifications from Chilli Notify via WebSocket.

- Fully automated launch with Lua script.

## ⚙️ Возможности
- Фильтрация доходов - не подключается к серверам, если доход брейнрота в секунду ниже указанного порога в конфиге.

- Интеграция с Discord - использует токен Discord для прослушивания сообщений от Chilli Notify через WebSocket.

- Полностью автоматический запуск с помощью скрипта Lua.

## 📥 Installation
1. Install Python 3.12 or higher:
https://www.python.org/downloads/

2. Download or clone the repository.

3. Run `setup.bat` - it will automatically install all dependencies.

4. Wait for the installation to complete and configure the config.py file:
- Specify the value of `MONEY_THRESHOLD` (in millions, example: 1.3).
- Insert your `DISCORD_TOKEN`:
https://www.youtube.com/results?search_query=how+to+get+discord+token

5. Go to the `data/` folder, find the `joiner.lua` file, and copy it to the `AutoExec` folder of your executor.

6. Run `start.bat`.

7. Controls:
- F2 - pause/resume the script.

## 📥 Установка
1. Установите Python 3.12 или выше:
https://www.python.org/downloads/

2. Загрузите или клонируйте репозиторий.

3. Запустите `setup.bat` - он автоматически установит все зависимости.

4. Дождитесь завершения установки и настройте файл config.py:
- Укажите значение `MONEY_THRESHOLD` (в миллионах, например: 1.3).
- Вставьте свой `DISCORD_TOKEN`:
https://www.youtube.com/results?search_query=how+to+get+discord+token

5. Перейдите в папку `data`, найдите файл `joiner.lua` и скопируйте его в папку `AutoExec` вашего екзекьютора.

6. Запустите `start.bat`.

7. Управление:
- F2 - приостановить/возобновить скрипт.

## ⭐ Project support / Поддержка проекта

- If you found this script useful, please give it a star ⭐ on the repository. This motivates me to develop it further and create new projects.
- Если этот скрипт оказался вам полезным, пожалуйста, поставьте мне звездочку ⭐ в репозитории. Это мотивирует меня на его дальнейшее развитие и создание новых проектов.
- FREE FOREVER / ФРИ ФОРЕВА