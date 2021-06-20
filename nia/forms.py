from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask_login import current_user
from nia.models import User, Device,Telemetry



class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_username(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NewdeviceForm(FlaskForm):
    devicename = StringField('Device Name', validators=[DataRequired()])
    deviceIP = StringField('Device URL', validators=[DataRequired()])
    devicemethod = SelectField('Set Method', coerce=int ,validators=[DataRequired()])
    submit = SubmitField('Save')

    def validate_username(self, device_IP):
        device = Device.query.filter_by(device_IP=device_IP.data).first()
        if device:
            raise ValidationError('IP address already exists')




