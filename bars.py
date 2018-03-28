import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)
    pass


def get_biggest_bar(data):
    seats = []
    for feature in data['features']:
        seats.append(feature['properties']['Attributes']['SeatsCount'])
    max_seats = max(seats)
    for feature in data['features']:
        if feature['properties']['Attributes']['SeatsCount'] == max_seats:
            print("The biggest bar is: {name}, seats: {seats}".format(name=feature['properties']['Attributes']['Name'], seats=max_seats))
    pass


def get_smallest_bar(data):
    seats = []
    for feature in data['features']:
        seats.append(feature['properties']['Attributes']['SeatsCount'])
    min_seats = min(seats)
    for feature in data['features']:
        if feature['properties']['Attributes']['SeatsCount'] == min_seats:
            print("The smallest bar is: {name}, seats: {seats}".format(name=feature['properties']['Attributes']['Name'], seats=min_seats))
    pass


def get_closest_bar(data, longitude, latitude):
    pass


def main():
    data = load_data('bars.json')
    get_biggest_bar(data)
    get_smallest_bar(data)


if __name__ == '__main__':
    main()
    pass
