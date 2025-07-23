import requests
import time
import json

# === CONFIGURATION ===
TELEGRAM_TOKEN = "7220790083:AAGBFHieTApaz53T9aXL9-aflZ1vSGE3zPk"
TELEGRAM_CHAT_ID = "1123042948"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    print(f"✅ Sent alert: {message}")
    return response.json()

# 🔁 NEW: Pull alerts from online hosted JSON
def load_signals():
    try:
        url = "https://forexinsight.ai/users/maryorwahmi/signals.json"  # LIVE LINK COMING SHORTLY
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print("❌ Error loading signals:", e)
        return []

sent_alerts = set()

while True:
    alerts = load_signals()
    for signal in alerts:
        msg = signal["message"]
        if msg not in sent_alerts:
            send_alert(msg)
            sent_alerts.add(msg)
    print("⏱ Waiting 5 minutes...")
    time.sleep(300)
