import requests
import os

etf_list = {
    "00403A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=63YTW",
    "00981A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=49YTW",
    "00988A": "https://www.ezmoney.com.tw/ETF/Fund/AssetExcelNPOI?fundCode=61YTW"
}

# 在當前資料夾建立一個下載資料夾
os.makedirs("downloads", exist_ok=True)

for name, url in etf_list.items():
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f"downloads/{name}.xlsx"
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ {name} 下載完成並存入 downloads 資料夾")
