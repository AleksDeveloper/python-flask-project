import sqlite3
import json

def selectAllfromTable(database, table):
    try:
        connectionDB = sqlite3.connect(database)
        response = connectionDB.execute("SELECT * FROM " + table)
        responselist = []
        for row in response:
            print(row,"entro")
            responselist.append(row)
        print(responselist)
        #jsonlist = json.dumps(str(responselist))
        #print("JSON: " + jsonlist)
        json_object = json.loads(responselist)
        createJsonFile("request1.json", json_object)
        return responselist
    except sqlite3.Error as e:
        print("ERROR: " + str(e))
    
def createJsonFile(name, value):
    f = open(name, "w")
    json.dump(str(value), f, indent=6)
    f.close()