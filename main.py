import time
import requests

WEBHOOK_URL = "https://hook.us2.make.com/u3xbx4mf2gdgu4bt9vrq9a3o433hgf0i"

def run_webhook():
    try:
        res = requests.post(WEBHOOK_URL, json={"auto": True}, timeout=10)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Status: {res.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        run_webhook()
        time.sleep(300)  # 5분 간격
