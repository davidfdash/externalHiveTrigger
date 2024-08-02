import jaydebeapi

# Connection parameters
jdbc_url = 'jdbc:hive2://knox.host:8443/default'  # JDBC URL for HiveServer2
username = 'your-username'
password = 'your-password'
jar_file = '/path/to/hive-jdbc-driver.jar'  # Path to the Hive JDBC driver JAR file

# Establish connection to Hive
conn = jaydebeapi.connect(
    'org.apache.hive.jdbc.HiveDriver',
    jdbc_url,
    [username, password],
    jar_file
)

# Create cursor
cursor = conn.cursor()

# Execute Hive query
cursor.execute('SELECT * FROM hive_table')

# Fetch results
result = cursor.fetchall()

# Close cursor and connection
cursor.close()
conn.close()