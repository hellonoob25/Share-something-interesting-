import time
import requests

webhook_url = "你的 Discord Webhook URL"
for i in range(100):
    data = {"content": f"這是第 {i+1} 條訊息"}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 429:  # 被限制
        retry_after = response.json().get('retry_after', 5)
        print(f"被限制，等待 {retry_after} 秒")
        time.sleep(retry_after)
    else:
        print(f"已送出第 {i+1} 條訊息，狀態碼：{response.status_code}")
        time.sleep(2)  # 建議設為 1 秒或以上
