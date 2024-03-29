import os
from flask import session, Flask, redirect, render_template, request, flash, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from dbutils import dbUtils
from dataclasses import dataclass, fields
from forms.forms import CreateTableForm, HTMLEmailSendForm, InsertForm, LoginForm, PresetTables, SignUpForm, DeleteForm, UpdateForm, SearchForm, EmailSendForm
from model import User, getUser, users, getUser2, createFromDB
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from emailutils.emailUtils import send_email_mul_att, send_email_as_html
from dotenv import load_dotenv
load_dotenv()
from os import getenv
from flask_ckeditor import CKEditor
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alejandrodjc'
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "You need to be logged in to view this page, please log in."
login_manager.login_message_category = "warning"
ckeditor = CKEditor(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # HERE IS THE MAGIC - COMPARISON
        if dbUtils.select_from_table("dbutils/db1.db", "users2", "user", "user", str(form.user.data)) is not None:
            #Create the existent user temporarily in the users model
            user2 = createFromDB(form.user.data)
            user = getUser(form.user.data)
            if user2 is not None and user2.check_password(form.password.data):
                users.append(user2)
                login_user(user2, remember=form.remember_me.data, force=True, fresh=False)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('home')
                flash("User: " + str(form.user.data) + " logged in successfully", "success")
                return redirect(next_page)
            else:
                flash("Password for user: " + str(form.user.data) + " is incorrect.", "warning")
        else:
            flash("User: " + str(form.user.data) + " doesn't exist.", "warning")        
        # HERE ENDS THE MAGIC - COMPARISON

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.name.data
        user = form.user.data
        email = form.email.data
        password = form.password.data
        birthdate = form.birthdate.data
        gender = form.gender.data
        #User Creation and Save
        if dbUtils.select_from_table("dbutils/db1.db", "users2", "user", "user", user) is None and dbUtils.select_from_table("dbutils/db1.db", "users2", "email", "email", email) is None:
            user_created = User(len(users) + 1, name, user, email, password, birthdate, gender)
            users.append(user_created)
            dbUtils.insert_full_table("dbutils/db1.db", "users2", user_created)
            #Keep user logged in
            login_user(user_created, remember=True)
            flash("User " + str(user) + " registered and logged in.", "success")
        else:
            flash("User " + str(user) + "  or email " + str(email) + " already registered. Please, try again.", "warning")
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


@app.route("/table2")
@login_required
def table2():
    form = InsertForm()
    form2 = DeleteForm()
    form3 = UpdateForm()

    response = dbUtils.select_all_from_table("dbutils/db1.db","users")
    headers = response[:1]
    data = response[1:]
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
            flash(user + " " + msg, 'success')
            return redirect(url_for("table2"))

@app.route('/deletionWTForms', methods = ["POST"])
def deletionWTForms():
    form2 = DeleteForm()
    id = form2.id.data          
    if request.method == 'POST':
        dbUtils.delete_registry("dbutils/db1.db", "users", "id", id)
        flash(id + " deleted successfully.", "warning")
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
    if request.method == 'POST':
        dbUtils.update_registry("dbutils/db1.db", "users", "id", updated.id, updated)
        flash(updated.id + " modified successfully.", "info")
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
    return redirect(url_for('table', model = model, year = year, limit = limit))

@app.route('/table3')
def table3(**kwargs):
    form = SearchForm()
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
    
    return table3(make=make, model=model, year=year, cylinders=cylinders, fuel_type=fuel_type, drive=drive, limit=limit)

@app.route('/table4')
def table4(**kwargs):
    form = CreateTableForm()
    formPreset = PresetTables()
    url = kwargs.get('url')
    headers = kwargs.get('headers')
    if kwargs.get('columns') is None:
        columns = [""]
    else:
        columns = kwargs.get('columns')
    pdf = kwargs.get('pdf')
    excel = kwargs.get('excel')
    copy = kwargs.get('copy')
    if kwargs.get('presetURL') is not None and kwargs.get('presetColumns') is not None:
        presetURL = kwargs.get('presetURL')
        presetColumns = kwargs.get('presetColumns')
    else:
        presetURL = ""
        presetColumns = ""
    if kwargs.get('tableTitle') is not None:
        tableTitle = kwargs.get('tableTitle')
    else:
        tableTitle = "Custom Table"

    return render_template('table4.html', form=form, formPreset=formPreset, url=url, headers=headers, columns=columns, pdf=pdf, excel=excel, 
                           copy=copy, presetColumns=presetColumns, presetURL=presetURL, tableTitle=tableTitle)

@app.route('/table4update', methods=["POST"])
def table4update():
    form = CreateTableForm()
    formPreset = PresetTables()

    preset = formPreset.preset.data

    presetURL = ""
    presetColumns = ""
    tableTitle = ""
    if preset is not None:
        query = dbUtils.select_all_from_table_where("dbutils/db1.db","presets","name",str(preset))
        presetURL = query[1:][0][2]
        presetColumns = query[1:][0][3]
        tableTitle = query[1:][0][1] + " Table"

    url = form.url.data
    headers = form.headers.data
    columns = form.columns.data
    pdf = form.pdf.data
    excel = form.excel.data
    copy = form.copy.data

    copy = "copy" if copy == True else ""
    pdf = "pdf" if pdf == True else ""
    excel = "excel" if excel == True else ""
    
    if columns is not None:
        columns = columns.split(', ')

    return table4(url=url, headers=headers, columns=columns, pdf=pdf, excel=excel, copy=copy, presetColumns=presetColumns, presetURL=presetURL, tableTitle=tableTitle)

@app.route('/email', methods=['GET', 'POST'])
def email():
    form = EmailSendForm()
    sender = senderPassword = recipient = subject = message = attachments = ""

    if form.validate_on_submit():
        sender = form.sender.data
        senderPassword = form.senderPassword.data
        recipient = form.recipient.data
        recipientsList = recipient.split(";")
        subject = form.subject.data
        message = form.message.data
        attachments = form.attachment.data
        attachmentsList = []
        if(attachments[0].filename != ""):
            for attachment in attachments:
                attachment.save(str(os.environ.get("MY_UPLOADS_PATH")) + attachment.filename)
                attachmentsList.append(str(os.environ.get("MY_UPLOADS_PATH")) + attachment.filename)
        status = send_email_mul_att(sender, senderPassword, recipientsList, subject, message, attachmentsList)
        if status != "OK":
            flash("ERROR: " + str(status), "danger")
        elif status == "OK":
            flash("Email sent from: " + str(sender) + " to " + str(recipient), "success")
    return render_template('email.html', form=form, sender=sender, senderPassword=senderPassword, recipient=recipient, subject=subject, message=message, attachments=attachments)

@app.route('/email2', methods=['GET', 'POST'])
def email2():
    form = HTMLEmailSendForm()
    sender = senderPassword = recipient = subject = message = attachments = ""

    if form.validate_on_submit():
        sender = form.sender.data
        senderPassword = form.senderPassword.data
        recipient = form.recipient.data
        recipientsList = recipient.split(';')
        subject = form.subject.data
        message = form.message.data
        attachments = form.attachment.data
        attachmentsList = []
        # if not os.path.exists(str(getenv("MY_UPLOADS_PATH"))):
        #     os.makedirs(str(os.getenv("MY_UPLOADS_PATH")))
        #     print("Folder created successfully")
        if not os.path.exists(str(os.environ.get('MY_UPLOADS_PATH'))):
            os.makedirs(str(os.environ.get('MY_UPLOADS_PATH')))
            print("Folder created successfully")
        else:
            print("Folder already exists")
        if(attachments[0].filename != ""):
            for attachment in attachments:
                attachment.save(str(os.environ.get("MY_UPLOADS_PATH")) + attachment.filename)
                #attachment.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), str(getenv("MY_UPLOADS_PATH")), secure_filename(attachment.filename)))
                #attachmentsList.append(str(getenv("MY_UPLOADS_PATH")) + secure_filename(attachment.filename))
                attachmentsList.append(str(os.environ.get('MY_UPLOADS_PATH')) + attachment.filename)
                print("LIST IS: ", attachmentsList)
        status = send_email_as_html(sender, senderPassword, recipientsList, subject, message, attachmentsList)
        if status != "OK":
            flash("ERROR: " + str(status), "danger")
        elif status == "OK":
            flash("Email sent from: " + str(sender) + " to " + str(recipient), "success")
    return render_template('email2.html', form=form, sender=sender, senderPassword=senderPassword, recipient=recipient, subject=subject, message=message, attachments=attachments)