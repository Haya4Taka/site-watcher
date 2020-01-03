from src.domain.interface.property_usecase_i import PropertyUsecaseI
from src.domain.model.property import Property
from src.usecases.interface.property_repository_i import PropertyRepositoryI

class PropertyUsecaseImpl(PropertyUsecaseI):
    property_repository: PropertyRepositoryI

    def __init__(self, repository: PropertyRepositoryI):
        self.property_repository = repository

    def register(self, url: str) -> Property:
        return self.property_repository.register(url)
