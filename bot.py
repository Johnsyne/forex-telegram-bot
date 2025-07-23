import requests
import time

# === CONFIGURATION ===
TELEGRAM_TOKEN = "7220790083:AAGBFHieTApaz53T9aXL9-aflZ1vSGE3zPk"
TELEGRAM_CHAT_ID = "1123042948"

# === FUNCTION: Send Telegram Message ===
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

# === LOOP: Send Sample Alerts Every 5 Minutes (for now) ===
sent_alerts = set()

def get_new_forex_alerts():
    return [
        "📢 *EURUSD Alert*: Testing 1.0935 resistance 🔥",
        "📢 *USDJPY Alert*: Price hit 159.80 ✅ Target: 160.40"
    ]

while True:
    alerts = get_new_forex_alerts()
    for alert in alerts:
        if alert not in sent_alerts:
            send_alert(alert)
            sent_alerts.add(alert)
    print("Waiting 5 minutes...")
    time.sleep(300)  # 5 minutes
