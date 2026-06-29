import requests
import os
import sys

# 1. 設定你的 ETF 下載清單 (保留原有的)
etf_list = {
    "00403A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=63YTW",
    "00981A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=49YTW",
    "00988A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=61YTW"
}

def download_etf():
    os.makedirs("downloads", exist_ok=True)
    for name, url in etf_list.items():
        response = requests.get(url)
        if response.status_code == 200:
            file_path = f"downloads/{name}.xlsx"
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"✅ {name} 下載完成")

# 2. 主程式：判斷是「定時任務」還是「指令任務」
if __name__ == "__main__":
    # 取得從 GitHub Actions 傳入的命令
    command = sys.argv[1] if len(sys.argv) > 1 else ""

    if not command:
        # 當 command 是空的，表示是 schedule (定時) 觸發
        print("--- 執行每日定時下載任務 ---")
        download_etf()
    else:
        # 當有 command，表示是 Telegram 指令觸發
        print(f"--- 處理指令: {command} ---")
        if "ETF" in command:
            download_etf()
            print("資料已下載，請至 GitHub Artifacts 下載。")
        else:
            print("收到其他指令，目前尚未開發...")
