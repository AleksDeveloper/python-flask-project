from flask import session, Flask, redirect, render_template, request, flash, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from dbutils import dbUtils
from dataclasses import dataclass, fields
from forms.forms import InsertForm, LoginForm, SignUpForm, DeleteForm, UpdateForm, SearchForm
from model import User, getUser, users, getUser2, createFromDB
from werkzeug.urls import url_parse
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alejandrodjc'
login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.route("/")
def home():
    print(current_user)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        print("\nLOGINENTRO\n")
        # HERE IS THE MAGIC - COMPARISON
        if dbUtils.selectfromTable("dbutils/db1.db", "users2", "user", "user", str(form.user.data)) is not None:
            #Create the existent user temporarily in the users model
            user2 = createFromDB(form.user.data)
            print(user2)
            print("comparo password de user: ", user2.getPassword() + "\n Con el form: " + form.password.data)
            print("Valido la password con hash: ", user2.check_password(form.password.data))
            user = getUser(form.user.data)
            #user2 = getUser2(user, form.user.data)
            print("USER:" + str(user) + "\nUSER 2: " + str(user2))
            if user2 is not None and user2.check_password(form.password.data):
                users.append(user2)
                login_user(user2, remember=form.remember_me.data, force=True, fresh=False)
                print("CURRENT USER: ", current_user)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('home')
                flash("Usuario " + str(form.user.data) + "logueado con éxito", "success")
                return redirect(next_page)
            else:
                flash("La contraseña para el usuario " + str(form.user.data) + " es incorrecta.", "warning")
        else:
            flash("Usuario " + str(form.user.data) + " no existe.", "warning")        
        # HERE ENDS THE MAGIC - COMPARISON

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    try:
        print("USERS ES:",users)
        print(users[0].getPassword())
    except IndexError as e:
        print("INDEXERROR: ", str(e))
    if form.validate_on_submit():
        print("ENTRO AL SUBMIT SIGNUP")
        name = form.name.data
        user = form.user.data
        email = form.email.data
        password = form.password.data
        birthdate = form.birthdate.data
        gender = form.gender.data
        #User Creation and Save
        if dbUtils.selectfromTable("dbutils/db1.db", "users2", "user", "user", user) is None and dbUtils.selectfromTable("dbutils/db1.db", "users2", "email", "email", email) is None:
            print("ENTRO PORQUE NO EXISTE USUARIO O EMAIL")
            user_created = User(len(users) + 1, name, user, email, password, birthdate, gender)
            users.append(user_created)
            print(user_created)
            print(type(user_created))
            print(user_created.getUser())
            print("\n Your password is:", user_created.getPassword())
            dbUtils.insertFullTable("dbutils/db1.db", "users2", user_created)
            #Keep user logged in
            login_user(user_created, remember=True)
        else:
            flash("Usuario " + str(user) + "  o email " + str(email) + " ya registrados. <br> Por favor, intenta con otros", "warning")
            return render_template("signup.html", form=form)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("signup.html", form=form)

if __name__ == '__main__':
    app.run()

@login_manager.user_loader
def loadUser(userID):
    for user in users:
        if user.id == int(userID):
            return user
    return None

@app.route("/table1")
@login_required
def table():
    form = SearchForm()
    model = ""
    year = ""
    limit = ""
    print (len(str((request))))
    print(request)
    #keys = ['model', 'year', 'limit']
    #for k in keya
    if(len(str(request))) > 46:
        model = request.args['model']
        year = request.args['year']
        limit = request.args['limit']
    print(model, year, limit)
    
    return render_template('table.html', form=form, model=model, year=year, limit=limit)

@app.route("/table2")
def table2():
    form = InsertForm()
    form2 = DeleteForm()
    form3 = UpdateForm()

    response = dbUtils.selectAllfromTable("dbutils/db1.db","users")
    print("YOUR RESPONSE", response)
    headers = response[:1]
    data = response[1:]
    print("YOUR HEADERS:", type(headers), headers)
    print("YOUR DATA:", type(data), data)
    return render_template('table2.html', headers = headers, data = data, form = form, form2 = form2, form3 = form3)

@app.route("/addrec", methods = ["POST", "GET"])
def addrec():
    form = InsertForm()
    if request.method == "POST":
        try:
            user = form.user.data
            password = form.password.data
            worker = form.worker.data
            student = form.student.data
            incomes = form.incomes.data
            print(user, password, worker, student, incomes, type(incomes))

            with sqlite3.connect("dbutils/db1.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (user, password, worker, student, incomes) VALUES (?,?,?,?,?)", (user, password, worker, student, float(incomes)))
                con.commit()
                msg = "successfully added"
                con.close()
        except sqlite3.Error as e:
            con.rollback()
            msg = "ERROR in insert operation " + str(e)
            con.close()

        finally:
            print("RESULT OF SQL OPERATION: " + msg)
            flash(user + " " + msg, 'success')
            flash("Este flash es un demo del info", 'info')
            return redirect(url_for("table2"))

@app.route('/deletionWTForms', methods = ["POST"])
def deletionWTForms():
    form2 = DeleteForm()
    id = form2.id.data                                                                        
    if request.method == 'POST':
        dbUtils.deleteRegistry("dbutils/db1.db", "users", "id", id)
        flash(id + " deleted successfully", "warning")
    return redirect(url_for('table2'))        

@app.route('/update', methods = ["POST"])
def update():
    form3 = UpdateForm()

    @dataclass
    class Registry:
        id: str
        user: str
        password: str
        worker: int
        student: int
        incomes: float

    updated = Registry(form3.id.data, form3.user.data, form3.password.data, int(form3.worker.data), int(form3.student.data), form3.incomes.data)

    print("\n\n\n" + updated.id, updated.user, updated.password, updated.worker, updated.student, updated.incomes, "\n\n")
    print(type(form3.student.data), type(updated.student))
    print("Converted:? ", str(int(updated.student)))
    print(updated)

    # for field in fields(updated2):
    #     print(field.name, getattr(updated2, field.name))
    # print("\n\nFinishedLooping\n\n")

    if request.method == 'POST':
        dbUtils.updateRegistry("dbutils/db1.db", "users", "id", updated.id, updated)
        flash(updated.id + " modified successfully", "info")
    return redirect(url_for('table2'))

@app.route('/tableupdate', methods = ["POST"])
def tableupdate():
    form = SearchForm()
    model = form.model.data
    year = form.year.data
    limit = form.limit.data
    session['model'] = model
    session['year'] = year
    session['limit'] = limit
    print(model, year, limit)
    #args kwargs
    return redirect(url_for('table', model = model, year = year, limit = limit))

@app.route('/table3')
def table3(**kwargs):
    form = SearchForm()
    #THIS APPROACH (line below) DOESNT SHOW AN ERROR IF model DOESNT EXIST
    print("TABLE3\n", kwargs.get('make'), kwargs.get('fuel_type'), kwargs.get('drive'))
    print(kwargs)
    print(type(kwargs))
    #THIS APPROACH (line below) SHOWS AN ERROR IF model DOESNT EXIST
    #print(kwargs["model"])
    for value in kwargs.values():
        print(value, end=" ")
    for key in kwargs.keys():
        print(key, end=" ")
    #Strings de búsqueda en Python - Medium
    make = kwargs.get('make')
    model = kwargs.get('model')
    year = kwargs.get('year')
    cylinders = kwargs.get('cylinders')
    fuel_type = kwargs.get('fuel_type')
    drive = kwargs.get('drive')
    limit = kwargs.get('limit')
    return render_template('table3.html', form=form, make=make, model=model, year=year, cylinders=cylinders, fuel_type=fuel_type, drive=drive, limit=limit)

@app.route('/table3update', methods=["POST"])
def table3update():
    form = SearchForm()
    
    make = form.make.data
    model = form.model.data
    year = form.year.data
    cylinders = form.cylinders.data
    fuel_type = form.fuel_type.data
    drive = form.drive.data
    limit = form.limit.data
    
    #return redirect(url_for('table3', make=make, model=model, year=year, cylinders=cylinders, fuel_gas=fuel_gas, fuel_diesel=fuel_diesel, fuel_electricity=fuel_electricity, limit=limit))
    return table3(make=make, model=model, year=year, cylinders=cylinders, fuel_type=fuel_type, drive=drive, limit=limit)



