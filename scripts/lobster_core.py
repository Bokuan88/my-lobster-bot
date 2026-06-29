import os
import requests
import sys

print("--- 龍蝦程式開始執行 ---")

# 檢查變數是否讀取到
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

print(f"DEBUG: Token 長度: {len(TOKEN) if TOKEN else '未讀取到!'}")
print(f"DEBUG: Chat ID: {CHAT_ID if CHAT_ID else '未讀取到!'}")

if not TOKEN or not CHAT_ID:
    print("❌ 錯誤：找不到 Token 或 Chat ID，請檢查 Secrets 設定！")
    sys.exit(1)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": "🦞 小龍蝦測試報告：我活過來了！"}

try:
    response = requests.post(url, data=payload)
    print(f"Telegram 回應狀態碼: {response.status_code}")
    print(f"Telegram 回應內容: {response.text}")
except Exception as e:
    print(f"發生網路錯誤: {e}")

print("--- 龍蝦程式執行結束 ---")
