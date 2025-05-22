#!/bin/bash

echo "🛑 Beende alle Coden-Komponenten..."

# Suche und beende Flask-Listener
pkill -f listener.py

# Suche und beende ngrok
pkill -f ngrok

# Optional: run_task oder andere Prozesse
pkill -f run_task.py

echo "✅ Alle Komponenten wurden beendet."
