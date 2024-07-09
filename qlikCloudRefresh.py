import config
import json
import requests


def refresh_data():
    url = config.cloud_url + "api/v1/reloads"
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
