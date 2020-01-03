from dataclasses import dataclass

@dataclass
class Room:
    __status: str
    __type: str
    __name: str
    __size: str
    __rent_fee: str
    __other_fee: str

    def get_status(self):
        return self.__status

    def get_type(self):
        return self.__type

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_rent_fee(self):
        return self.__rent_fee

    def get_other_fee(self):
        return self.__other_fee

    status = property(get_status)
    type = property(get_type)
    name = property(get_name)
    size = property(get_size)
    rent_fee = property(get_rent_fee)
    other_fee = property(get_other_fee)
