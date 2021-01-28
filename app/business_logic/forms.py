from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('username',validators = [InputRequired(),Length(min=4,max=20)])
    password = PasswordField('password',validators = [InputRequired(),Length(min=8,max=100)])

class SignupForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('lastname')
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=100)])
    confirmpassword = PasswordField('confirmpassword', validators=[InputRequired(), Length(min=8, max=100)])