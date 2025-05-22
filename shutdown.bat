@echo off
echo ==============================
echo   Beende Listener & ngrok
echo ==============================

:: Beende Flask Listener
taskkill /F /IM python.exe /T

:: Beende ngrok
taskkill /F /IM ngrok.exe /T

echo ✅ Alle Prozesse wurden beendet.
pause
