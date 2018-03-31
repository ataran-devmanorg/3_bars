# Ближайшие бары

Скрипт для осуществления выборок из списка баров.

Позволяет:

* Найти бар с наименьшим количеством посадочных мест.
* Найти бар с максимальным количеством посадочных мест.
* Найти бар ближайший к заданным координатам.

# Как запустить

## Зависимости скрипта

* Python 3
* Python modules
  * pip
  * json
  * geopy
  * click

## Параметры скрипта

```bash
$ python bars.py --help

Usage: bars.py [OPTIONS]

Options:
  -f, --file TEXT         Json file with bars info.
  -c, --coordinates TEXT  Your coordinates.
  --help                  Show this message and exit.
```

## Запуск скрипта без параметров

Параметры скрипта поумолчанию:

* file = bars.json
* coordinates = '0.0, 0.0'

```bash
$ python bars.py

The biggest bar is: Спорт бар «Красная машина», seats: 450.
The smallest bar is: БАР. СОКИ, seats: 0.
The closest bar to your location: (0.0, 0.0) is: Staropramen, distance: 6983.33 km.
```

## Запуск скрипта с параметрами

```bash
$ python bars.py -f bars.json -c '55.755799, 37.617678'

The biggest bar is: Спорт бар «Красная машина», seats: 450.
The smallest bar is: БАР. СОКИ, seats: 0.
The closest bar to your location: (55.755799, 37.617678) is: Коктейль-бар, distance: 0.19 km.
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
