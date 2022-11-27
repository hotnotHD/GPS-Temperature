import requests

from sender import Sender

if __name__ == '__main__':
    cities_dict = {"0": [55.7, 37.6], "1": [40.7, -74.0], "2": [38.9, -77.0], "3": [34.1, -118.2], "4": [52.5, 13.4]}
    send = Sender()
    choose = ""

    while choose != "3":
        nul_ok = True
        city_ok = True
        choose_ok = True
        temp_ok = True
        city_ok_name = True

        while choose_ok:
            print("Введите: 0-ввод GPS координат, 1-выбор из списка городов, 2-узнать GPS координаты города, 3-выход")
            choose = input()
            if choose in ["0", "1", "2", "3"]:
                choose_ok = False

        lat = 0
        long = 0
        if choose != "3":
            if choose == "0":
                while nul_ok:
                    print("latitude:")
                    lat = input()
                    print("longitude:")
                    long = input()

                    send.constructor(lat, long)

                    file = send.time_n_temp()
                    if file != "error":
                        nul_ok = False
                    else:
                        print("Неверный формат ввода")

            elif choose == "1":
                while city_ok:
                    print("Введите")
                    print("0-Moscow")
                    print("1-New York")
                    print("2-Washington")
                    print("3-Los Angeles")
                    print("4-Berlin")
                    city = input()
                    try:
                        lat = cities_dict[city][0]
                        long = cities_dict[city][1]
                        send.constructor(lat, long)
                        file = send.time_n_temp()
                    except KeyError:
                        print("Введите номер предложенного города")
                    else:
                        city_ok = False

            if choose == "2":
                while city_ok_name:
                    print("Введите название города")
                    city = input()
                    re = requests.get(f"https://nominatim.openstreetmap.org/?city={city}&format=json&limit=1")
                    try:
                        print(re.json()[0]["lat"])
                        print(re.json()[0]["lon"])
                    except IndexError:
                        print("Город введен неверно")
                    else:
                        city_ok_name = False

            if choose != "2":
                day = "0"
                while temp_ok:
                    print("Введите: 0 - для показа средней температуры за 7 дней, 1-7 - за 1 из 7 дней:")
                    day = input()
                    if day in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                        temp_ok = False
                    else:
                        print("Введите число от 0 до 7")

                print("Mid temperature: " + str(round(send.mid_temp(day), 2)))
