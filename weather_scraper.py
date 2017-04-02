from urllib.request import Request, urlopen, URLError
import json

request = Request('https://api.darksky.net/forecast/b5891a1d9eb7cf063c356b5747ae8d1c/45.520978, -122.677572')
try:
    response = urlopen(request)
    weather = response.read()
    weather_dict = json.loads(weather)

    print('The Current Temperature at 5th and Oak Max: ' + str(weather_dict['currently']['temperature']) + ' Degrees(F)')
    weather = weather[282:288]


except URLError:
    print('-NO WEATHER FOUND-')