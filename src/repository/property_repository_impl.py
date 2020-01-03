from src.usecases.interface.property_repository_i import PropertyRepositoryI
from src.domain.model.property import Property
from src.domain.model.room import Room
from bs4 import BeautifulSoup
import requests
import re

class PropertyRepositoryImpl(PropertyRepositoryI):
    def find(self, url: str) -> Property:

        r = requests.get(url)
        r_text = r.text
        soup = BeautifulSoup(r_text, 'lxml')

        name = soup.find('h1', class_='house_name').text
        nearby_station_array = [elm for elm in soup.find('table', attrs={'summary': '物件概要'}).tr.td.text.split('\t') if
                                elm != '']
        nearby_stations = ', '.join(nearby_station_array)
        vacant_rooms = []
        for tr in soup.find('table', attrs={'summary': '部屋詳細'}).tbody.find_all('tr', class_=False):
            tds = tr.find_all('td')
            status = re.sub(r'[\t\n]', '', tds[0].text)
            rent_fee = tds[7].text.replace('\t', '')
            other_fee = tds[8].text.replace('\t', '')
            vacant_rooms.append(Room(status, tds[1].text, tds[4].text, tds[3].text, rent_fee, other_fee))

        return Property(url, name, nearby_stations, vacant_rooms)