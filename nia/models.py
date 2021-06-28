from nia import login_manager, db
from flask_login import  UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable = False)
    email = db.Column(db.String(128), unique = True, nullable = False)
    is_active = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(128), unique= False, nullable = False)
    devices = db.relationship('Device', backref = 'owner')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    def is_active(self):
        return True

class Device(db.Model):
    __tablename__='device'
    id = db.Column(db.Integer, primary_key=True)
    decive_IP = db.Column(db.String(256), unique=True, nullable = True)
    device_name = db.Column(db.String(60), unique=False, nullable = True)
    device_method = db.Column(db.String(20), nullable=False)
    api_key = db.Column(db.String(256), unique=True, nullable=True)
    telemetrys = db.relationship('Telemetry', backref='device_data')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Device('{self.unique_tag}', '{self.decive_IP}' ,'{device_name}', '{device_method}','{self.api_token}')"

class Methods(db.Model):
    __tablename__='methods'
    id = db.Column(db.Integer, primary_key=True)
    method_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"Methods('{self.device_method}')"

class Telemetry(db.Model):
    __tablename__='telemetry'
    id = db.Column(db.Integer, primary_key=True)
    watts_in = db.Column(db.SmallInteger, unique=False, nullable = False)
    watts_out = db.Column(db.SmallInteger, unique=False, nullable = False)
    op_volt = db.Column(db.SmallInteger, unique=False, nullable = False)
    op_amp = db.Column(db.SmallInteger, unique=False, nullable = False)
    device_temp = db.Column(db.SmallInteger, unique=False, nullable = False)
    battery_temp = db.Column(db.SmallInteger, unique=False, nullable = False)
    fan_state = db.Column(db.String(128), unique=False, nullable = False)
    timestamp = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

    def __repr__(self):
        return f"Telemetry('{self.watts_in}', '{self.watts_out}', '{self.op_volt}', '{self.op_amp}','{self.device_temp}', '{self.battery_temp}','{self.enegry_state}', '{self.fan_state}','{self.timestamp}')"

