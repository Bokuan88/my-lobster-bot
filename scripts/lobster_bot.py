import requests
import os

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_msg(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": text})

def get_updates():
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    data = requests.get(url).json()
    if data['result']:
        last_msg = data['result'][-1]['message']['text']
        update_id = data['result'][-1]['update_id']
        return last_msg, update_id
    return None, None

# 簡單的邏輯：如果輸入代號，就去下載或查詢；如果是新聞，就去爬蟲
msg, uid = get_updates()
if msg:
    if msg.startswith("新聞"):
        send_msg("🦞 正在為您整理今日財經重點...")
        # 這裡未來可以串接 Google Search API 或新聞爬蟲
    else:
        send_msg(f"🦞 收到指令：查詢 {msg}。正在處理並儲存資料...")
        # 在這裡呼叫你的下載函數
