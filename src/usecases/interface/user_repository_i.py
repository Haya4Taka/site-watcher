from abc import ABCMeta, abstractmethod
from src.domain.model.user import User

class UserRepositoryI(metaclass=ABCMeta):
    @abstractmethod
    def get(self, id: str) -> User:
        pass

    def get_all(self) -> [User]:
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
