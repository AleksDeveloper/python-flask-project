import sqlite3

db = input("db: ")
table = input("table: ")
field = input("field: ")
value = input("value: ")
try:
    connectionDB = sqlite3.connect(db)
    response = connectionDB.cursor()
    response.execute("DELETE FROM " + table + " WHERE " + field + " = ?", (value))
    connectionDB.commit()
    connectionDB.close()
    print("Deleted")
except sqlite3.Error as e:
    print("ERROR: " + str(e))