from sender import Sender


if __name__ == '__main__':
    send = Sender()
    print("latitude:")
    lat = input()
    print("longitude:")
    long = input()
    send.constructor(lat, long)

    file = send.time_n_temp()

    print(file)
    print(file[0])
    print(file[1])

    print("Middle temperature (0 - 7 days, 1-7 - day from today):")
    day = input()
    print("Mid temperature: " + str(send.mid_temp(day)))


