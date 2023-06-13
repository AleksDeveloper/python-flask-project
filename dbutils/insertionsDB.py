import sqlite3

connectionDB = sqlite3.connect("db1.db")
user = str(input("User:"))
password = str(input("Password:"))
worker = str(input("Worker? (1=YES, 0=NO):"))
student = str(input("Student? (1=YES, 0=NO):"))
incomes = str(input("Incomes:"))
print(user, password, worker, student, incomes)

try:
    connectionDB.execute("INSERT INTO users (user, password, worker, student, incomes) values (?,?,?,?,?)", (user, password, worker, student, incomes))
    connectionDB.commit()
    connectionDB.close()
except sqlite3.Error as e:
    print("ERROR: " + e)
