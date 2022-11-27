from sender import Sender

# Создан класс для отправки и получения запросов, добавлена обработка приходящих json #4
# Расчет среднего значения температуры за 7 дней и за один из 7

if __name__ == '__main__':
    cities_dict = {"0": [55.7, 37.6], "1": [40.7, -74.0], "2": [38.9, -77.0], "3": [34.1, -118.2], "4": [52.5, 13.4]}
    send = Sender()
    print("0-input gps coordinates, 1-choose from list of cities")
    choose = input()
    lat = 0
    long = 0
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

    send.constructor(lat, long)

    file = send.time_n_temp()

    print(file)
    print(file[0])
    print(file[1])

    print("Middle temperature (0 - 7 days, 1-7 - day from today):")
    day = input()
    print("Mid temperature: " + str(send.mid_temp(day)))


