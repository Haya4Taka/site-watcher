from dataclasses import dataclass, field
from src.domain.model.room import Room
from typing import List

@dataclass
class Property:
    __url: str
    __name: str
    __nearby_stations: str
    __vacant_rooms: List[Room] = field(default_factory=list)

    def get_url(self):
        return self.__url

    def get_name(self):
        return self.__name

    def get_nearby_station(self):
        return self.__nearby_stations

    def get_vacant_rooms(self):
        return self.__vacant_rooms

    # 宣言的にプライベート変数を取得
    url = property(get_url)
    name = property(get_name)
    nearby_station = property(get_nearby_station)
    vacant_rooms = property(get_vacant_rooms)

    def has_vacant_room(self):
        return len(self.vacant_rooms) != 0
