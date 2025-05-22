import requests
import json

LUNA_ENDPOINT = "http://localhost:5005/execute"

def ask_luna(messages=None, prompt=None, format="json", model="mistral"):
    payload = {
        "model": model,
        "format": format
    }

    if messages:
        payload["messages"] = messages
    elif prompt:
        payload["prompt"] = prompt
    else:
        raise ValueError("Entweder 'messages' oder 'prompt' muss gesetzt sein.")

    try:
        response = requests.post(LUNA_ENDPOINT, json=payload, timeout=60)
        response.raise_for_status()
        return response.json().get("response", "[Keine Antwort erhalten]")
    except requests.exceptions.RequestException as e:
        return f"[Fehler bei Anfrage an Luna]: {str(e)}"
