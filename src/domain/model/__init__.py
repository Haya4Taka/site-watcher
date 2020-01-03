from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from src.domain.model.user import User

__all__ = [
    User,
]