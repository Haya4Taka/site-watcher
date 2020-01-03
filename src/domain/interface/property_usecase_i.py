from abc import ABCMeta, abstractmethod
from src.domain.model.property import Property

class PropertyUsecaseI(metaclass=ABCMeta):
    @abstractmethod
    def find(self, url: str) -> Property:
        pass

