from dataclasses import dataclass
from src.domain.model import db
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import PasswordType
from flask_marshmallow import Marshmallow
# from init import app
from werkzeug.security import generate_password_hash, check_password_hash

# ma = Marshmallow(app)

# @dataclass
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512'
        ]
    ), nullable=False)
    destination = Column(String(255), default=None)

    def __repr__(self):
        return 'User<%r, %r, %r>' % (self.id, self.email, self.destination)

class UserSchema(ma.Schema):
    class Meta:
        fields = ["id", "email", "destination"]

user_schema = UserSchema()
users_schema = UserSchema(many=True)