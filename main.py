import config
import pandas as pd
import qseowRefresh
from sqlalchemy import create_engine
from datetime import date

today = (date.today())
lastrefresh = ""


# Check the Hive database for a True value
def isitdone():
    conn = f'hive://{config.user_name}:{config.passwd}@{config.host_server}:{config.port}/{config.database}'
    engine = create_engine(conn, connect_args={'auth': 'LDAP'})

    query = "select case when ar.ts>br.ts then true else false end as status from ea_common.channel_hive_table_info_br br INNER JOIN ea_common.channel_hive_table_info_ar ar on br.tablename=ar.tablename where ar.tablename='chnlptnr_sellin_fact';"
    data = pd.read_sql(query, con=engine)
    print(data)
    global lastrefresh
    lastrefresh = date.today()

# main function
def main():
    global lastrefresh
    while lastrefresh != today:
        isitdone()
    qseowRefresh.refresh_data()

main()