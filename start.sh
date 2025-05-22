#!/bin/bash

echo "🚀 Starte Coden + Luna Aurelia Core Umgebung..."

# 1. Starte lokalen Listener
echo "📡 Starte API-Listener auf http://localhost:5005 ..."
gnome-terminal -- bash -c "python3 listener.py; exec bash" 2>/dev/null || x-terminal-emulator -e "python3 listener.py" &

sleep 2

# 2. Starte ngrok für mobilen Zugriff
echo "🌐 Starte ngrok (falls installiert)..."
if command -v ngrok &> /dev/null
then
  gnome-terminal -- bash -c "ngrok http 5005; exec bash" 2>/dev/null ||   x-terminal-emulator -e "ngrok http 5005" &
else
  echo "⚠️  Ngrok nicht gefunden. Bitte manuell starten falls benötigt."
fi

# 3. Optional: Test an Luna-Core senden
read -p "➡️  Direkt Testbefehl an Luna senden? (y/n): " test_choice
if [ "$test_choice" = "y" ]; then
  echo "🧪 Sende Beispiel-Prompt an Luna..."
  curl -X POST http://localhost:5005/execute \
    -H "Content-Type: application/json" \
    -d '{
      "prompt": "Gib mir 3 Ideen für ein inspirierendes Reel.",
      "model": "mistral"
    }'
fi

echo "✅ System läuft. Du kannst jetzt über AutoGPT oder das Handy Kommandos senden."
