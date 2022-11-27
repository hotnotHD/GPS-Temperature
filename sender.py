import requests


class Sender:

    def __init__(self):
        self.base = "https://api.open-meteo.com/v1/forecast?"
        self.latitude = "latitude=59.94"
        self.longitude = "longitude=30.31"
        self.hourly = "hourly=temperature_2m"
        self.timezone = "timezone=Europe%2FMoscow"
        self.str_to_send = ""

    def constructor(self, lat, long):
        self.latitude = f"latitude={lat}"
        self.longitude = f"longitude={long}"
        self.str_to_send = f"{self.base}{self.latitude}&{self.longitude}&{self.hourly}&{self.timezone}"

    def send_n_receive(self):
        re = requests.get(self.str_to_send)
        return re

    def time_n_temp(self):
        json = self.send_n_receive().json()
        time = json["hourly"]["time"]
        temp = json["hourly"]["temperature_2m"]
        return [time, temp]

    def mid_temp(self, setting):
        j = 0
        max = 24
        if setting == "0":
            max = 24 * 7
        else:
            j = int(setting)

        [times, temps] = self.time_n_temp()

        mid = 0
        for i in range(max):
            mid += temps[i + j*24]
        mid /= max
        return mid

