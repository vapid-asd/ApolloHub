import requests
import time


while True:
    url = "https://discord.com/api/v9/channels/814889219008102450/messages"
    headers = {
        "Authorization": "your token here",
        "Content-Type": "application/json"
    }
    data = {
        "content": "!work"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200 or response.status_code == 204:
        print("Message sent successfully")
    time.sleep(3600)
