import config
import qseowRefresh
import jaydebeapi
import datetime
import time


# Check the Hive database for a True value
def isitdone():
    # Replace with your database details
    driver = "org.apache.hive.jdbc.HiveDriver"
    jdbc_url = "jdbc:hive2://hnr02n04-i.hpeit.hpecorp.net:8443/;ssl=true;transportMode=http;httpPath=gateway/cdp-proxy-api/hive"
    credentials = ["srvc_eapqlik_sls_hitg", "*****"]
    jar_path = "E:/Scripts/externalHiveTrigger-master/JDBC Jar for Hive/hive-jdbc-uber-2.6.5.0-292.jar"

    # Connect to the database
    conn = jaydebeapi.connect(driver, jdbc_url, credentials, jar_path)

    # Create a cursor
    curs = conn.cursor()

    # Execute a query
    curs.execute(
        "select case when ar.ts>br.ts then true else false end as status from ea_common.channel_hive_table_info_br br INNER JOIN ea_common.channel_hive_table_info_ar ar on br.tablename=ar.tablename where ar.tablename='chnlptnr_sellin_fact'")

    # Fetch the results
    results = curs.fetchall()

    # Print the results
    for row in results:
        print(row[0])
        doneornot = row[0]
    # Close the cursor and connection
    curs.close()
    conn.close()
    return doneornot


# main function


def main():
    lastrefresh = "2024-08-10"
    #runtoday = False
    while True:
        while not isitdone():
            print('not done at ' + str(datetime.datetime.now()))
            time.sleep(600)
        while lastrefresh != datetime.date.today():# and not runtoday:
            lastrefresh = qseowRefresh.refresh_data()
            print('refresh run at ' + str(datetime.datetime.now()))
            #runtoday = True
        time.sleep(600)


main()
