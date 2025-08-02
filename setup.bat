@echo off
title Library installation

echo [EN] Installing required libraries...
echo [EN] If errors occur: 1) Reinstall Python 2) Check "Add to PATH"
echo.
echo [RU] Ustanovka bibliotek...
echo [RU] Esli oshibki: 1) Pereustanovite Python 2) Vibirete "Dobavit v PATH"
echo.

pip install -r requirements.txt

echo.
echo [EN] Complete. Run start.bat
echo [RU] Gotovo. Zapustite start.bat

pause