from src.domain.interface.user_usecase_i import UserUsecaseI
from src.usecases.interface.user_repository_i import UserRepositoryI
from src.domain.model.user import User

class UserUseaseImpl(UserUsecaseI):
    user_repository: UserRepositoryI

    def __init__(self, repository: UserRepositoryI):
        self.user_repository = repository

    def save(self, user: User):
        self.user_repository.save(user)

    def get_all(self) -> [User]:
        return self.user_repository.get_all()

