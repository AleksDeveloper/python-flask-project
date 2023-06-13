from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dbutils import dbUtils

class User(UserMixin):

    def __init__(self, id, name, user, email, password, birthdate, gender, is_admin=False):
        self.id = id
        self.name = name
        self.user = user
        self.email = email
        self.password = generate_password_hash(password)
        self.birthdate = birthdate
        self.gender = gender
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        print("\n\n Will compare: ", self.password, "with: ", password)
        return check_password_hash(self.password, password)
    
    def getName(self):
        return self.name

    def getUser(self):
        return self.user
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getBirthdate(self):
        return self.birthdate
    
    def getGender(self):
        return self.gender
    
    def __repr__(self):
        return '<User {}>'.format(self.email)
    
class UserLogin(UserMixin):

    def __init__(self, id, name, user, email, passwordEncrypted, birthdate, gender, is_admin=False):
        self.id = id
        self.name = name
        self.user = user
        self.email = email
        self.password = passwordEncrypted
        self.birthdate = birthdate
        self.gender = gender
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        print("\n\n Will compare: ", self.password, "with: ", password)
        return check_password_hash(self.password, password)
    
    def getName(self):
        return self.name

    def getUser(self):
        return self.user
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getBirthdate(self):
        return self.birthdate
    
    def getGender(self):
        return self.gender
    
    def __repr__(self):
        return '<User {}>'.format(self.email)
    
users = []

def createFromDB(user):
    print("\nCREARÉ A ESTE PERRO: ", user)
    data = dbUtils.selectAllfromTableWhere("dbutils/db1.db", "users2", "user", str(user))
    print("\n Quiero acceder a name: ", data[1:][0][1])
    print("\n Quiero acceder a password: ", data[1:][0][4])
    name = str(data[1:][0][1])
    email = str(data[1:][0][3])
    password = str(data[1:][0][4])
    gender = str(data[1:][0][5])
    birthdate = str(data[1:][0][6])
    tempUser = UserLogin(len(users) + 1, name, str(user), email, password, birthdate, gender)
    return tempUser

def getUser(user):
    for user1 in users:
        if user1.user == user:
            return user1
    return None

def getUser2(which, user):
    userreturn = dbUtils.selectfromTable("dbutils/db1.db", "users2", str(which), "user", str(user))
    return userreturn

