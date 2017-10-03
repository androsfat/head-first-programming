import sqlite3

db = sqlite3.connect("surfersDB.sdb")

db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("select * from surfers")
rows = cursor.fetchall()

for row in rows:
    if row['id'] == 104:
        print("ID is:         " + str(row['id']))
        print("Name is:       " + row['name'])
        print("Board-type id: " + row['board'])

cursor.close()
