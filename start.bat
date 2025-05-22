@echo off
echo ========================================
echo   Starte Coden + Luna Aurelia Core
echo ========================================

:: Aktiviere Python Umgebung (falls nötig)
cd /d C:\Coden Project

echo [1/3] Starte Listener...
start cmd /k "python listener.py"

timeout /t 3 >nul

echo [2/3] Starte ngrok (falls installiert)...
where ngrok >nul 2>nul
if %errorlevel%==0 (
    start cmd /k "ngrok http 5005"
) else (
    echo ⚠️  ngrok.exe nicht gefunden. Bitte manuell starten, falls benötigt.
)

echo [3/3] System ist bereit. Du kannst jetzt Aufgaben senden.
pause
