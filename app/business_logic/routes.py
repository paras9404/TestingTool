from app import app
from app import db
from flask import request, session, redirect, render_template, url_for, flash
from .models import User
from .forms import LoginForm, SignupForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                login_user(user)
                return render_template('dashboard.html', form=form)
        flash('Invalid Username or Password', 'danger')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        if form.password.data != form.confirmpassword.data :
            flash('Passwords do not match! Try again.', 'danger')
            return redirect(url_for('signup'))
        hashed_password = generate_password_hash(form.password.data,method='sha256')
        print(form.username.data)
        new_user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data,email=form.email.data, password=hashed_password, confirmpassword=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('index'))


