# GPS-Temperature
Определение температуры по GPS координатам

Консольное приложение для получения средней температуры по GPS координатам.

## Возможности
1. Получение средней температуры за 7 дней.
2. Получение средней температуры за 1 день на выбор.
3. Получение температуры по координатам.
4. Выбор города из списка.
5. Возможность узнать координаты города.

## Тестирование
main - [![Tests for GPS-Temperature](https://github.com/hotnotHD/GPS-Temperature/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/hotnotHD/GPS-Temperature/actions/workflows/python-app.yml)   
develop - [![Tests for GPS-Temperature](https://github.com/hotnotHD/GPS-Temperature/actions/workflows/python-app.yml/badge.svg?branch=develop)](https://github.com/hotnotHD/GPS-Temperature/actions/workflows/python-app.yml)

## Запуск

Для запуска необходимо клонировать репозиторий, установить библиотеки из файла `requirements.txt`
и запустить программу:
```
$ python3 main.py
```
## Docker

Для запуска программы в Docker необходимо перейти в папку `src` и выполнить команды:
```
$ sudo docker build -t gps .
```
Запуск: 
```
$ sudo docker run -it gps
```

## Пример работы

Вывод средней температуры по координатам:
```
$ sudo docker run -it gps
Введите: 0-ввод GPS координат, 1-выбор из списка городов, 2-узнать GPS координаты города, 3-выход
0
latitude:
10
longitude:
10
Введите: 0 - для показа средней температуры за 7 дней, 1-7 - за 1 из 7 дней:
0
Mid temperature: 24.72
```
Получение координат города:
```
$ sudo docker run -it gps
Введите: 0-ввод GPS координат, 1-выбор из списка городов, 2-узнать GPS координаты города, 3-выход
2
Введите название города
Москва
55.7504461
37.6174943
```