from application import db, login_manager
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Posts', backref='author', lazy=True)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))