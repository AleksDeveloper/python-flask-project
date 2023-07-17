import sqlite3

def selectAllfromTable(db, table):
    try:     
        connectionDB = sqlite3.connect(db)
        response = connectionDB.cursor()
        response.execute("SELECT * FROM " + table)
        #Give me the columns
        col_name_list = [tuple[0] for tuple in response.description]
        print("Your columns: ", col_name_list)
        col_name_tuple = tuple(col_name_list)
        print("Your new columns: ", col_name_tuple)
        #Create a list to append columns
        responseList = []
        responseList.append(col_name_tuple)
        #append data from response
        for row in response:
            responseList.append(row)
        #close Database 
        connectionDB.close()
        return responseList
    except sqlite3.Error as e:
        print("ERROR: ", str(e))

def selectAllfromTableWhere(db, table, where, value):
    try:
        connectionDB = sqlite3.connect(db)
        response = connectionDB.cursor()
        response.execute("SELECT * FROM " + table + " WHERE " + where + " = " + "'" + str(value) + "'")
        #Give me the columns
        col_name_list = [tuple[0] for tuple in response.description]
        print("Your columns: ", col_name_list)
        col_name_tuple = tuple(col_name_list)
        print("Your new columns: ", col_name_tuple)
        #Create a list to append columns
        responseList = []
        responseList.append(col_name_tuple)
        #append data from response
        for row in response:
            responseList.append(row)
        #close Database
        connectionDB.close()
        return responseList
    except sqlite3.Error as e:
        print("ERROR: ", str(e))

def selectfromTable(db, table, value, where, data):
    try:
        connectionDB = sqlite3.connect(db)
        response = connectionDB.cursor()
        response.execute("SELECT " + value + " FROM " + table + " WHERE " + where + " = " + "'"+data+"'")
        return response.fetchall()[0][0]

    except sqlite3.Error as e:
        print("ERROR: ", str(e))
    except IndexError as i:
        print("INDEX ERROR: ", str(i))


def insertFullTable(db, table, data):
    if db=="dbutils/db1.db" and table=="users2":
        try:
            connectionDB = sqlite3.connect(db)
            response = connectionDB.cursor()
            response.execute("INSERT INTO " + table + "(name, user, email, password, gender, birthdate) VALUES (?,?,?,?,?,?)", (data.getName(), data.getUser(), data.getEmail(), data.getPassword(), data.getGender(), data.getBirthdate()))
            connectionDB.commit()
            connectionDB.close()
        except sqlite3.Error as e:
            print("ERROR: " + e)
    else:
        print("THE DATABASE OR TABLE DOESN'T EXIST")

def createDB(db):
    try:
        connectionDB = sqlite3.connect(db)
    except sqlite3.Error as e:
        print("ERROR: " + e)

def deleteRegistry(db, table, field, value):
    try:
        connectionDB = sqlite3.connect(db)
        response = connectionDB.cursor()
        response.execute("DELETE FROM " + table + " WHERE " + field + " = ?", (str(value),))
        connectionDB.commit()
        connectionDB.close()
    except sqlite3.Error as e:
        print("ERROR: " + str(e))

def updateRegistry(db, table, where, valueWhere, values):
    try:
        connectionDB = sqlite3.connect(db)
        response = connectionDB.cursor()
        response.execute("UPDATE " + table + " SET " + "user = '" + str(values.user) + "', password = '" + str(values.password) + "', worker = '" + str(values.worker) + "', student = '" + str(values.student) + "', incomes = '" + str(values.incomes) + "' WHERE " + where + " = " + valueWhere)
        connectionDB.commit()
        connectionDB.close()
    except sqlite3.Error as e:
        print("ERROR: " + e)



