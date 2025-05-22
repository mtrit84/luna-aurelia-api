@echo off
echo ==============================
echo   Starte ngrok Tunnel
echo ==============================

:: Starte Tunnel für Port 5005
start cmd /k "ngrok http 5005"

echo ✅ ngrok wird gestartet. Kopiere die URL aus dem Terminal.
pause
