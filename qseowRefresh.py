import config
import json
import requests


def refresh_data():
    url = config.cloud_url + "/qrs/task/" + config.taskId + "/start/synchronous"
    headers = {
        'Authorization': 'Bearer ' + config.api_key,
        'Content-type': 'application/json'
    }
    payload = json.dumps({
        "appId": config.appId,
        "partial": False
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(url)
    print(headers)
    print(payload)
    print(response.text)


refresh_data()
