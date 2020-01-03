from src.usecases.interface.user_repository_i import UserRepositoryI
from src.domain.model.user import User
from src.domain.model import db

class UserRepositoryImpl(UserRepositoryI):
    def get(self, id: str):
        return User.query.filter_by(id=id).first()

    def get_all(self) -> [User]:
        return User.query.all()

    def save(self, user: User):
        db.session.add(user)
        db.session.commit()

    def update(self, new_user: User):
        user = User.query.filter_by(id=User.id).first()
        user = new_user
        db.session.commit()

    def delete(self, id: id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

