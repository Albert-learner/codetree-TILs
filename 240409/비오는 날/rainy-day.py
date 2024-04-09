N = int(input())

class WEATHER:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    def print_weather(self):
        print(self.date, self.day, self.weather)

weathers = []
for _ in range(N):
    date, day, weather = input().split()
    weathers.append(WEATHER(date, day, weather))

weathers = sorted(weathers, key = lambda x: x.date)
rain_weathers = [whr for whr in weathers if whr.weather == "Rain"]
rain_weathers[0].print_weather()