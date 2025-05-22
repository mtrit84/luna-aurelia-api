from flask import Flask, request, jsonify
import subprocess
import logging
import json
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "execution_log.json"

def log_entry(entry):
    with open(LOG_FILE, "a") as f:
        json.dump(entry, f)
        f.write("\n")

@app.route("/execute", methods=["POST"])
def execute_command():
    data = request.get_json()
    origin = data.get("origin")
    command = data.get("command")
    params = data.get("params", {})

    if origin not in ["AutoGPT", "Martin Tritschler", "LunaGPT"]:
        return jsonify({"status": "unauthorized", "error": "Invalid origin"}), 403

    timestamp = datetime.now().isoformat()
    log_data = {
        "timestamp": timestamp,
        "origin": origin,
        "command": command,
        "params": params,
        "status": "started"
    }

    try:
        if command == "create_reel":
            cmd = ["python3", "run_task.py", "--task", command, "--params", json.dumps(params)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            log_data["status"] = "success" if result.returncode == 0 else "error"
            log_data["stdout"] = result.stdout
            log_data["stderr"] = result.stderr
        else:
            log_data["status"] = "error"
            log_data["stderr"] = f"Unknown command: {command}"
    except Exception as e:
        log_data["status"] = "exception"
        log_data["stderr"] = str(e)

    log_entry(log_data)
    return jsonify(log_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
