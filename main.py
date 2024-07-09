import time
import json
import requests
import config
import pandas as pd
from sqlalchemy import create_engine

#reload the app specified in config
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
#    print(url)
#    print(headers)
#    print(payload)
    print(response.text)


#Check the Hive database for a True value
def isItDone():
    while True:
        conn = f'hive://{config.user_name}:{config.passwd}@{config.host_server}:{config.port}/{config.database}'
        engine = create_engine(conn, connect_args={'auth': 'LDAP'})

        query = "select case when ar.ts>br.ts then true else false end as status from ea_common.channel_hive_table_info_br br INNER JOIN ea_common.channel_hive_table_info_ar ar on br.tablename=ar.tablename where ar.tablename='chnlptnr_sellin_fact';"
        data = pd.read_sql(query, con=engine)
        print(data)
        return data


#def main():





refresh_data()
