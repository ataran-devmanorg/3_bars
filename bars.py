import json
from geopy import distance


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)
    pass


def get_biggest_bar(data):
    seats = []
    for feature in data['features']:
        seats.append((feature['properties']['Attributes']['Name'], feature['properties']['Attributes']['SeatsCount']))
    max_seats = max(seats, key=lambda t: t[1])
    print("The biggest bar is: {name}, seats: {seats}.".format(name=max_seats[0], seats=max_seats[1]))


def get_smallest_bar(data):
    seats = []
    for feature in data['features']:
        seats.append((feature['properties']['Attributes']['Name'], feature['properties']['Attributes']['SeatsCount']))
    min_seats = min(seats, key=lambda t: t[1])
    print("The smallest bar is: {name}, seats: {seats}.".format(name=min_seats[0], seats=min_seats[1]))


def get_closest_bar(data, longitude, latitude):
    bars = []
    for feature in data['features']:
        long = feature['geometry']['coordinates'][1]
        lat = feature['geometry']['coordinates'][0]
        dist = round(distance.vincenty((longitude, latitude), (long, lat)).km, 2)
        bars.append((feature['properties']['Attributes']['Name'], dist))
        # print(feature['properties']['Attributes']['Name'], dist)
    closest_bar = min(bars, key=lambda t: t[1])
    print(closest_bar)
    pass


def main():
    data = load_data('bars.json')
    get_biggest_bar(data)
    get_smallest_bar(data)
    get_closest_bar(data, 0.0, 0.0)


if __name__ == '__main__':
    main()
    pass
