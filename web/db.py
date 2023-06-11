from mysql import connector

conn_params = {
    "user":"C1",
    "password":"secret",
    "host":"localhost",
    "port":"8081",
    "database":"SHOP"
}
connection = connector.connect(**conn_params)
cursor = connection.cursor()
# cursor.execute("DESC ITEMS")
print(cursor.fetchall())
cursor.close()
connection.close()
