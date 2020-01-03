import requests
from bs4 import BeautifulSoup
from src.domain.model.room import Room
import re
response = requests.get("http://www.guesthousebank.com/a_detail/q_11765/")
# response = requests.get("http://www.guesthousebank.com/a_detail/q_11819/")
r_text = response.text
soup = BeautifulSoup(r_text, 'lxml')

nearby_station_array = [elm for elm in soup.find('table', attrs={'summary': '物件概要'}).tr.td.text.split('\t') if elm != '']
nearby_stations = ', '.join(nearby_station_array)
print(nearby_stations)
# print(nearby_station.split('\t'))

# print(nearby_station.replace('\t', '', 10))

# tbody = soup.find('table', attrs={'summary': '部屋詳細'}).tbody
# vacant_rooms = []
# for tr in tbody.find_all('tr', class_=False):
#     tds = tr.find_all('td')
#     vacant_rooms.append(Room(tds[1].text, tds[4].text, tds[3].text, tds[7].text, tds[8].text))
# print(len(vacant_rooms))