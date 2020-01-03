from src.domain.model import db
from sqlalchemy import Column, Integer, String

class UserProperty(db.Model):
    __tablename__ = 'user-property'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    url = Column(String(255), nullable=False)