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
