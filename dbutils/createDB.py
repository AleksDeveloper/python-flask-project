import sqlite3

connectionDB = sqlite3.connect("db1.db")

# try:
#     connectionDB.execute("""create table if not exists users (
#                                                 id integer primary key autoincrement,
#                                                 user text,
#                                                 password text,
#                                                 worker bool,
#                                                 student bool,
#                                                 incomes real
#                                                 )""")
#     print("************\nTABLE users CREATED\n*************")
# except sqlite3.OperationalError as e:
#     print("ERROR: "+e)
# connectionDB.close()

# try:
#     connectionDB.execute("""CREATE TABLE IF NOT EXISTS users2 (
#                                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                                 name TEXT,
#                                                 user TEXT,
#                                                 email TEXT,
#                                                 password TEXT,
#                                                 gender TEXT,
#                                                 birthdate DATE
#                                                 )""")
#     print("************\nTABLE users2 CREATED\n************")
# except sqlite3.OperationalError as e:
#     print ("ERROR: " + str(e))
# connectionDB.close()

try:
    connectionDB.execute("""CREATE TABLE IF NOT EXISTS presets (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                name TEXT,
                                                url TEXT,
                                                columns TEXT
                                                )""")
    print("***********\nTABLE presets CREATED\n****************")
except sqlite3.OperationalError as e:
    print("ERROR: " + str(e))

# try:
#     connectionDB.execute("DROP TABLE presets")
#     connectionDB.commit()
#     print("TABLE presets DELETED")
# except sqlite3.OperationalError as e:
#     print("ERROR: " + str(e))

connectionDB.close()