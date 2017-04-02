from urllib.request import Request, urlopen, URLError
import json
from bs4 import BeautifulSoup
request = Request('https://api.darksky.net/forecast/b5891a1d9eb7cf063c356b5747ae8d1c/45.520978, -122.677572')
try:
    response = urlopen(request)
    weather = response.read()
    weather_dict = json.loads(weather)

    print('The Current Temperature at 5th and Oak Max: ' + str(weather_dict['currently']['temperature']) + ' Degrees(F)')
    weather = weather[282:288]


except URLError:
    print('-NO WEATHER FOUND-')
request = Request('https://developer.trimet.org/ws/V1/arrivals?locIDs=7627&appID=6A7774DCD7E758D67350B4DC2')
try:
    response = urlopen(request)
    bustimes = response.read()
    xml_soup = BeautifulSoup(bustimes, 'xml')
    location = xml_soup.location['desc']
    print(location)
except URLError:
    print('NO BUS TIMES FOUND-')