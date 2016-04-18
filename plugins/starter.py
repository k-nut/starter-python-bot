# coding=utf-8

import re
import logging
crontable = []
outputs = []
typing_sleep = 0


SUPPORTED_CITIES = ["Berlin", "Erlangen", "Essen",
                    "Karlsruhe", "Köln", "Leipzig",
                    "Moers", "München", "Neu-Ulm",
                    "Paderborn", "Ulm", "Wuppertal"]
SUPPORTED_CITIES = [city.lower() for city in SUPPORTED_CITIES]



def process_message(data):
    """ Process the incoming message and reply cool things! """
    logging.debug("process_message:data: {}".format(data))
    location_regex = re.compile(r"Wo ist Markt in (?P<location>\w+)\?")

    matches = location_regex.match(data['text']).groupdict()
    if matches:
        location = matches.get('location')
        if location.lower() in SUPPORTED_CITIES:
            message = "https://wo-ist-markt.de/%s"
            outputs.append([data['channel'], message % location.lower()])
        else:
            message = "\n".join(["Es gibt keinen Markt in %s. Füge ihn doch hinzu!",
                                 "https://github.com/wo-ist-markt/wo-ist-markt.github.io"
                                ])
            outputs.append([data['channel'], message % location.lower()])
