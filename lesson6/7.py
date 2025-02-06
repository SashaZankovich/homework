"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

from pyowm import OWM

owm = OWM('cfc373a7f54c1efd4cc2c00873364a9f')
mgr = owm.weather_manager()

user = input('Введите город: ')

observation = mgr.weather_at_place(user)
w = observation.weather
temp = w.temperature('celsius')
wind = w.wind()

print(f"""
    Влажность воздуха: {w.humidity} %
    Температура воздуха: {temp.get('temp')} °C
    Скорость ветра: {wind.get('speed')} м/с
                                            """)