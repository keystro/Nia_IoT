from flask import render_template, url_for, session, flash, redirect, request, jsonify, Blueprint
from nia import db, login_manager
from nia.forms import  SignupForm, LoginForm, NewdeviceForm
from flask_login import login_user, current_user, logout_user, login_required
from nia.models import User, Device, Telemetry, Methods
import secrets, random


views = Blueprint('views',__name__)

@views.route('/')
@views.route('/index')
def index():
    return render_template('index.html')

@views.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            session['email'] = request.form['email']
            flash('Login Successful','success')
            return redirect(url_for('views.index'))
        else:
            flash('Login Unsuccessful. Please check your login details', 'danger')
    return render_template('login.html', form=form)

@views.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password= form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User account has been created successfully','success')
        return redirect(url_for('views.login'))
    return render_template('register.html', form=form)

@views.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('email', None)
    return redirect(url_for('views.index'))

@views.route('/account')
@login_required
def account():
    if current_user.is_authenticated:
        return render_template('account.html', username=username)
    else:
        flash('User Authentication required','danger')
        return redirect(url_for('views.login'))

@views.route('/adddevice', methods=['GET','POST'])
@login_required
def adddevice():
    if current_user.is_authenticated:
        groups = Methods.query.all()
        group_list=[(i.devicemethod, i.methodname) for i in groups]
        form = NewdeviceForm()
        form.devicemethod.choices=group_list
        device_key = generate_api_key()
        if form.validate_on_submit():
            device_data = Device(device_name=form.devicename.data, device_IP=form.deciveIP.data, device_method=form.devicemethod.data, api_key=device_key)
            db.session.add(device_data)
            db.session.commit()
            flash('Devive Channel Creation Successful', 'Success')
            return device_key
        return render_template('devices.html')
    else:
        flash('User Authentication required','danger')
        return redirect(url_for('views.login'))

def generate_api_key():
    aphrases=['Alpha','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whiskey','X-ray','Yankee','Zulu']
    alist=[]
    token = secrets.token_hex(24)
    alist.append(token)
    tag = random.choice(aphrases)+secrets.token_hex(4)
    alist.append(tag)
    sep = '/'
    key = sep.join(alist)
    return key

