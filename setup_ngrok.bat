@echo off
echo ================================
echo   Konfiguriere ngrok Authtoken
echo ================================

ngrok config add-authtoken 2xSBlBDkAXWSfaPKiW03whLZiMF_5KZF6CWYu9fkZHbMjCgtc

echo ✅ Token wurde gesetzt. Starte ngrok jetzt mit:
echo    ngrok http 5005
pause
