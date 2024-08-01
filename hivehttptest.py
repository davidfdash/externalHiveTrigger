from pyhive import hive
from thrift.transport.THttpClient import THttpClient
import base64
import config


def connect_to_pyhive():
    # Connects to Pyhive with HTTP mode
    conn = hive.connect(thrift_transport=add_http_mode_support())
    cursor = conn.cursor()
    cursor.execute("show databases")
    print (cursor.fetchone())


def add_http_mode_support(username=config.user_name, password=config.passwd, port=10001, httpPath="/cliservice", host=config.host_server, transportMode="http"):
    # Utility function which generate Transport client object which in turn can be passwd to hive connection to
    # establish the HTTP mode connection.
    ap = "%s:%s" % (username, password)
    transport = THttpClient(host, port=port, path=httpPath)
    transport.setCustomHeaders({"Authorization": "Basic " + base64.b64encode(ap).strip()})
    print(transport)
    return transport

if __name__ == '__main__':
    # connect_to_pyhive()
    add_http_mode_support()