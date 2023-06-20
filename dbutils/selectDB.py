import sqlite3
import dbUtils

data = dbUtils.selectAllfromTableWhere("../dbutils/db1.db", "users2", "user", "francisco")
print("\n Quiero acceder a name: ", data[1:][0][1])
print("\n Quiero acceder a password: ", data[1:][0][4])

connectionDB = sqlite3.connect("db1.db")
response = connectionDB.cursor()
#response.execute("SELECT * FROM users2")
#response.execute("SELECT user, email name FROM users2 WHERE user = 'alejadrodjc'")
response.execute("SELECT * FROM presets")
#print("THE RESPONSE AS NORMAL IS: ", response.fetchall()[0][1])


responselist = []
#*************************WE GET THE COLUMN NAMES INTO A LIST HERE***************************************
# col_name_list = [tuple[0] for tuple in response.description]
# print(col_name_list)
# responselist.append(list(col_name_list))


for row in response:
    print(row, "entro")
    responselist.append(row)


connectionDB.close()

print("FINAL LIST:\n", responselist)
print("\nI want to access a value NAME: ", responselist[0][1])



#print(responselist[1:])
#print(responselist[:1])




