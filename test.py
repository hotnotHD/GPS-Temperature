import requests

from src.sender import Sender

test_sender = Sender()
test_sender.constructor(10, 10)

broken_sender = Sender()
broken_sender.constructor(190, 2000)

test_url = "https://api.open-meteo.com/v1/forecast?latitude=10&longitude=10&hourly=temperature_2m&timezone=Europe%2FMoscow"
re = requests.get(test_url)
temps = re.json()["hourly"]["temperature_2m"]


def test_constructor():
    assert test_sender.str_to_send == test_url


def test_time_n_temp():
    assert test_sender.time_n_temp() == temps
    assert broken_sender.time_n_temp() == "error"


def test_mid_temp():
    mid = 0
    for i in range(24 * 7):
        mid += temps[i]
    mid /= (24 * 7)

    assert test_sender.mid_temp("0") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 0 * 24]
    mid /= 24

    assert test_sender.mid_temp("1") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 1 * 24]
    mid /= 24

    assert test_sender.mid_temp("2") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 2 * 24]
    mid /= 24

    assert test_sender.mid_temp("3") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 3 * 24]
    mid /= 24

    assert test_sender.mid_temp("4") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 4 * 24]
    mid /= 24

    assert test_sender.mid_temp("5") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 5 * 24]
    mid /= 24

    assert test_sender.mid_temp("6") == mid

    mid = 0
    for i in range(24):
        mid += temps[i + 6 * 24]
    mid /= 24

    assert test_sender.mid_temp("7") == mid


def test_send_n_receive():
    assert test_sender.send_n_receive().status_code == 200
