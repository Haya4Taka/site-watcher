from abc import ABCMeta, abstractmethod
from src.domain.model.user import User

class UserUsecaseI(metaclass=ABCMeta):
    @abstractmethod
    def save(self):
        pass

    def update(self):
        pass

    def get(self, id: str) -> User:
        pass

    def get_all(self) -> [User]:
        pass

    # def find(self) -> [User]:
    #     pass

    def register(self, url: str):
        pass
