import argparse
import json
from luna_core import create_reel

parser = argparse.ArgumentParser()
parser.add_argument("--task", required=True)
parser.add_argument("--params", required=True)

args = parser.parse_args()
params = json.loads(args.params)

if args.task == "create_reel":
    theme = params.get("theme", "Reichtum")
    voice = params.get("voice", "female")
    caption = params.get("caption", "Fülle")
    create_reel.create_reel(theme, voice, caption)
else:
    print(f"[❌] Unbekannter Task: {args.task}")
