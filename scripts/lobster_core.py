import requests
import os
import sys

def send_telegram_message(text):
    TOKEN = os.environ['TELEGRAM_TOKEN']
    CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def download_etf():
    # ... (原本的下載邏輯) ...
    try:
        # ... 你的下載程式碼 ...
        return True, "✅ ETF 成分表已下載完成，請去 GitHub Artifacts 下載！"
    except Exception as e:
        return False, f"❌ 下載失敗，原因：{str(e)}"

if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    
    if "ETF" in command:
        success, message = download_etf()
        send_telegram_message(message) # 這一行就是讓龍蝦回信的關鍵
    else:
        send_telegram_message("🦞 小龍蝦收到了，但我看不懂這條指令喔！")
