import os
import requests

# 這裡會讀取你在 GitHub 設定的 Secret
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ 訊息成功傳送！")
        else:
            print(f"❌ 傳送失敗，狀態碼：{response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"⚠️ 發生錯誤：{e}")

if __name__ == "__main__":
    send_message("🦞 嗨！我是你的線上小龍蝦，我已經成功被喚醒並連接到 Telegram 了！")
