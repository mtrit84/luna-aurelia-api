from gpt_bridge import ask_luna

def create_reel(theme, voice, caption):
    prompt = (
        f"Erstelle ein Skript für ein Instagram Reel zum Thema '{theme}', "
        f"mit einer weiblichen Stimme. Verwende die Caption: '{caption}'."
    )

    print("🎬 Frage Luna nach Skript...")
    reel_script = ask_luna(prompt=prompt, format="markdown")

    print("📜 Skript von Luna:")
    print(reel_script)

    with open("reel_script.md", "w", encoding="utf-8") as f:
        f.write(reel_script)

    return reel_script
