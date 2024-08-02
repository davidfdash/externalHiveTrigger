from pyhive import presto
from sqlalchemy import create_engine
import pandas as pd
import config

Presto_conn = presto.connect(host=config.host_server,
                             port=8014,
                             protocol='https',
                             requests_kwargs={'verify':False,'auth':(config.user_name, config.passwd)})
final_query = "select case when ar.ts>br.ts then true else false end as status from ea_common.channel_hive_table_info_br br INNER JOIN ea_common.channel_hive_table_info_ar ar on br.tablename=ar.tablename where ar.tablename='chnlptnr_sellin_fact';"
data = pd.read_sql(final_query, con=Presto_Conn)
print(data)

# engine = create_engine(conn, connect_args={'auth': 'LDAP'})
#    query = "select case when ar.ts>br.ts then true else false end as status from ea_common.channel_hive_table_info_br br INNER JOIN ea_common.channel_hive_table_info_ar ar on br.tablename=ar.tablename where ar.tablename='chnlptnr_sellin_fact';"
#    data = pd.read_sql(query, con=engine)
     print(data)
#    return data