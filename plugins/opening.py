import json
import os
import re

from osm_time.opening_hours import OpeningHours

DAYS = {"Montag": "mo",
        "Dienstag": "tu",
        "Mittwoch": "we",
        "Donnerstag": "th",
        "Freitag": "fr",
        "Samstag": "sa",
        "Sonntag": "su"}

def main():
    offen = match_text("Welcher Markt hat am Montag um 14:00 auf?")
    print offen

def match_text(text):
    data = get_data()
    markets = make_openings(data)
    pattern = re.compile(r".* (?P<weekday>\w+) um (?P<time>\d+:\d+).*")
    match = pattern.match(text)
    if match is None:
        print "Did not match"
        return None
    match_dict = match.groupdict()
    
    day = match_dict.get("weekday")
    time = match_dict.get("time")
    weekday = DAYS.get(day)
    if not weekday or not time:
        return
    return open_at(markets, weekday, time)


def open_at(markets, day, time):
    open_markets = []
    for market in markets:
        if market['opening_hours'].is_open(day, time):
            open_markets.append(market['name'])
    return open_markets


def make_openings(data):
    markets = []
    for market in data:
        opening_string = market["properties"].get("opening_hours")
        if opening_string is None:
            continue
        opening_hours = OpeningHours(opening_string)
        markets.append({'opening_hours': opening_hours,
                        'name': market["properties"].get("title")
                        })
    return markets

def get_data():
    path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(path, "../data/berlin.json")
    with open(data_path) as infile:
        data = json.load(infile)
        return data["features"]


if __name__ == "__main__":
    main()
