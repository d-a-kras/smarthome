import pgdb

try:
    conn = pgdb.connect(database='loval', host='localhost', port='5555',
                        user='postgres', password='kras')
except pgdb.Error as err:
    print("Connection error: {}".format(err))

sql = "SELECT * FROM shedules"
    
try:
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
except pgdb.Error as err:
    print("Query error: {}".format(err))
    
print(data)
6
