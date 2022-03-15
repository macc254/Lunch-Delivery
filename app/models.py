from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email= db.Column(db.String(255), unique=True, index= True)
    user_password=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())


    def __repr__(self):
        return f'User  {self.username}'

    @property
    def password(self):
        raise AttributeError("Password has no read attribute")
    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.user_password, password)
    
