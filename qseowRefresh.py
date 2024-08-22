import config
import json
import requests
import urllib3
from datetime import date


def refresh_data():
    # Set up necessary headers comma separated
    xrf = 'iX83QmNlvu87yyAB'
    headers = {'X-Qlik-xrfkey': xrf,
               "Content-Type": "application/json",
               "X-Qlik-User": config.user}

    # Set the endpoint URL
    endpoint = ':4242/qrs/task/' + config.taskId + '/start/synchronous'
    xrfk = '?xrfkey={}'.format(xrf)
    url = config.node + endpoint + xrfk
    # print(url)
    response = requests.post(url, headers=headers, verify=False, cert=config.cert)
    print(url)
    print(headers)
    print(response)
    print(response.text)
    lastrefresh = (date.today())
    return lastrefresh

urllib3.disable_warnings()
#refresh_data()
