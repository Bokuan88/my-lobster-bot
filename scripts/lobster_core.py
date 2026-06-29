import requests
import os

# 從 GitHub Secrets 抓取設定
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

# 這裡開始你的龍蝦任務
if __name__ == "__main__":
    message = "🦞 小龍蝦已啟動！今天有什麼任務要交給我嗎？"
    send_telegram_msg(message)
