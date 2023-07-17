from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, SelectField, EmailField, DateField, TextAreaField, MultipleFileField, FileField
from wtforms.validators import DataRequired, Email, InputRequired
from flask_ckeditor import CKEditorField

class InsertForm(FlaskForm):
    user = StringField('User', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    worker = BooleanField('Worker')
    student = BooleanField('Student')
    incomes = DecimalField('Incomes', validators = [DataRequired()])
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    id = StringField('Id')
    submit = SubmitField('Delete Registry')

class UpdateForm(FlaskForm):
    id = StringField('Id')
    user = StringField('User', validators = [DataRequired()])
    password = StringField('Password', validators = [DataRequired()])
    worker = BooleanField('Worker')
    student = BooleanField('Student')
    incomes = DecimalField('Incomes', validators = [DataRequired()])
    submit = SubmitField('Update Registry')

class SearchForm(FlaskForm):
    model = StringField('Model')
    year = DecimalField('Year')
    make = StringField('Make')
    cylinders = DecimalField('Cylinders')
    fuel_gas = BooleanField('Gasoline')
    fuel_diesel = BooleanField('Diesel')
    fuel_electricity = BooleanField('Electricity')
    limit = DecimalField('Limit')
    drive = SelectField('Drive', choices=[('fwd', 'front-wheel drive'), ('rwd', 'rear-wheel drive'), ('awd', 'all-wheel drive'), ('4wd', '4-wheel drive'), ('', 'all')])
    fuel_type = SelectField('Fuel Type', choices=[('gas', 'gasoline'), ('diesel', 'diesel'), ('electricity', 'electricity'), ('', 'all')])
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
    user = StringField('User or E-mail', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    name = StringField('Name', validators = [InputRequired()])
    user = StringField('User', validators = [InputRequired()])
    email = EmailField('E-mail', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])
    birthdate = DateField('Birth Date', validators = [InputRequired()])
    gender = SelectField('Gender', choices=[('male', 'male'), ('female', 'female'), ('idk', 'idk')])
    submit = SubmitField('Sign Up')

class CreateTableForm(FlaskForm):
    url = StringField('API URL Request', validators=[DataRequired()])
    headers = PasswordField('Auth Token', validators=[DataRequired()])
    columns = StringField('Columns', validators=[DataRequired()])
    pdf = BooleanField('Export to PDF')
    excel = BooleanField('Export to Excel')
    copy = BooleanField('Copy to clipboard')
    submit = SubmitField('Create Table')
    

class PresetTables(FlaskForm):
    preset = SelectField('Preset', choices=[('Calories by Activity', 'Calories by Activity'), ('Exercises by Muscle', 'Exercises by Muscle'),
                                            ('Inflation Type', 'Inflation Type'), ('Inflation Country', 'Inflation Country'), ('Cities in Country', 'Cities'),
                                            ('Emoji', 'Emoji')])
    submit = SubmitField('Fill Fields')

class EmailSendForm(FlaskForm):
    sender = EmailField('From Email', validators = [InputRequired()])
    senderPassword = PasswordField('Password', validators = [InputRequired()])
    recipient = StringField('Recipient(s)', validators = [InputRequired()])
    subject = StringField('Subject')
    message = TextAreaField('Message')
    attachment = MultipleFileField('Attachment(s)')
    singleAttachment = FileField('Attachment1')
    submit = SubmitField('Send Email')

class HTMLEmailSendForm(FlaskForm):
    sender = EmailField('From Email', validators = [InputRequired()])
    senderPassword = PasswordField('Password', validators = [InputRequired()])
    recipient = StringField('Recipient(s)', validators = [InputRequired()])
    subject = StringField('Subject')
    message = CKEditorField('Body')
    attachment = MultipleFileField('Attachment(s)')
    singleAttachment = FileField('Attachment1')
    submit = SubmitField('Send Email')
