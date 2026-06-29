import requests
import os
import sys

# 1. 設定你的 ETF 下載清單
etf_list = {
    "00403A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=63YTW",
    "00981A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=49YTW",
    "00988A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=61YTW"
}

def send_telegram_message(text):
    """發送訊息回 Telegram 的函數"""
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
    if not TOKEN or not CHAT_ID:
        print("❌ 無法發送 Telegram：缺少 Token 或 Chat ID")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

def download_etf():
    """執行下載任務的函數"""
    os.makedirs("downloads", exist_ok=True)
    success_files = []
    
    for name, url in etf_list.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                file_path = f"downloads/{name}.xlsx"
                with open(file_path, "wb") as f:
                    f.write(response.content)
                success_files.append(name)
                print(f"✅ {name} 下載完成")
        except Exception as e:
            print(f"❌ {name} 下載失敗: {e}")
            
    if success_files:
        return True, f"✅ 已成功下載: {', '.join(success_files)}，請至 GitHub Artifacts 下載。"
    else:
        return False, "❌ 所有 ETF 下載失敗，請檢查網址或網路狀況。"

if __name__ == "__main__":
    # 取得從 GitHub Actions 傳入的命令 (如果是排程觸發，command 會是空的)
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    
    print(f"--- 程式啟動，接收到的指令為: {command} ---")

    if not command or "ETF" in command:
        # 如果沒有指令 (排程) 或指令包含 "ETF"，執行下載
        success, message = download_etf()
        # 如果是指令觸發，才回傳給 Telegram
        if command:
            send_telegram_message(message)
        elif "新聞" in command:
        # 這裡模擬查詢動作
        result_text = "🦞 小龍蝦已執行新聞查詢：今日股市平穩，無重大波動。"
        send_telegram_message(result_text)
        print("✅ 新聞查詢指令處理完畢")
    else:
        # 收到其他不明指令
        send_telegram_message("🦞 小龍蝦已收到指令，但目前只學會幫您下載 ETF 成分表喔！")
