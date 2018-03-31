import json
from geopy import distance
import click


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


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
    closest_bar = min(bars, key=lambda t: t[1])
    print('The closest bar to your location: ({longitude}, {latitude}) is: {name}, distance: {distance} km.'.format(
        longitude=longitude, latitude=latitude, name=closest_bar[0], distance=closest_bar[1]))


@click.command()
@click.option('--file', '-f', default='bars.json', help='Json file with bars info.')
@click.option('--coordinates', '-c', default='0.0,0.0', help='Your coordinates.')
def main(file, coordinates):
    data = load_data(file)

    get_biggest_bar(data)
    get_smallest_bar(data)

    longitude = float(coordinates.split(',')[0])
    latitude = float(coordinates.split(',')[1])
    get_closest_bar(data, longitude, latitude)


if __name__ == '__main__':
    main()
