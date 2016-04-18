import time
import re
import random
import logging
crontable = []
outputs = []
attachments = []
typing_sleep = 0


SUPPORTED_CITIES = ["Berlin", "Erlangen", "Essen", "Karlsruhe", "Köln", "Leipzig", "Moers", "München", "Neu-Ulm", "Paderborn", "Ulm", "Wuppertal"]
SUPPORTED_CITIES = [city.lower() for city in cities]

location_regex = re.compile("Wo ist Markt in (?P<location>\w+)\?")
def process_message(data):
    logging.debug("process_message:data: {}".format(data))

    matches = location_regex.match(data['text']).groupdict()
    if matches:
        location = matches.get('location')
        if location.lower() in SUPPORTED_CITIES
            outputs.append([data['channel'], "https://wo-ist-markt.de/%s" % location.lower()])
        else:
            outputs.append([data['channel'], "Es gibt keinen Markt in %s. Füge ihn doch hinzu! https://github.com/wo-ist-markt/wo-ist-markt.github.io" % location.lower()])


