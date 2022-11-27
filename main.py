import requests

from sender import Sender

if __name__ == '__main__':
    cities_dict = {"0": [55.7, 37.6], "1": [40.7, -74.0], "2": [38.9, -77.0], "3": [34.1, -118.2], "4": [52.5, 13.4]}
    send = Sender()
    choose = ""
    while choose != "3":
        print("0-ввод GPS координат, 1-выбор из списка городов, 2-узнать GPS координаты города, 3-выход")
        choose = input()
        lat = 0
        long = 0
        if choose != "3":
            if choose == "0":
                print("latitude:")
                lat = input()
                print("longitude:")
                long = input()
            elif choose == "1":
                print("0-Moscow")
                print("1-New York")
                print("2-Washington")
                print("3-Los Angeles")
                print("4-Berlin")
                city = input()
                lat = cities_dict[city][0]
                long = cities_dict[city][1]
            if choose == "2":
                print("Введите название города на английском")
                city = input()
                re = requests.get(f"https://nominatim.openstreetmap.org/?city={city}&format=json&limit=1")
                print(re.json())
                print(re.json()[0]["lat"])
                print(re.json()[0]["lon"])
            send.constructor(lat, long)

            if choose != "2":
                file = send.time_n_temp()

                print("Middle temperature (0 - 7 days, 1-7 - day from today):")
                day = input()
                print("Mid temperature: " + str(send.mid_temp(day)))


