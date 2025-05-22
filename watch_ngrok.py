import requests
import time
import os

def get_ngrok_url():
    try:
        # Access ngrok's local API to retrieve tunnel information
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json().get("tunnels", [])
        for tunnel in tunnels:
            if tunnel["proto"] == "https":
                return tunnel["public_url"]
    except Exception as e:
        print(f"Fehler beim Abrufen der ngrok-URL: {e}")
    return None

def main():
    last_url = ""
    while True:
        url = get_ngrok_url()
        if url and url != last_url:
            last_url = url
            print(f"[+] Neue ngrok-URL erkannt: {url}")
            with open("current_ngrok_url.txt", "w") as f:
                f.write(url)
        time.sleep(5)

if __name__ == "__main__":
    print("🔍 Warte auf ngrok...")
    main()
