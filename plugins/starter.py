# coding=utf-8

import re
import logging

from opening import match_text
crontable = []
outputs = []
typing_sleep = 0


SUPPORTED_CITIES = [u"Berlin", u"Erlangen", u"Essen",
                    u"Karlsruhe", u"Köln", u"Leipzig",
                    u"Moers", u"München", u"Neu-Ulm",
                    u"Paderborn", u"Ulm", u"Wuppertal"]


def process_message(data):
    """ Process the incoming message and reply cool things! """
    logging.debug("process_message:data: {}".format(data))
    location_regex = re.compile(r"Wo ist Markt in (?P<location>\w+)\?")

    results = location_regex.match(data['text'])
    matches = results.groupdict() if results else None
    if matches:
        location = matches.get('location')
        if location.lower() in [city.lower() for city in SUPPORTED_CITIES]:
            message = "https://wo-ist-markt.de/#%s"
            outputs.append([data['channel'], message % location.lower()])
        else:
            message = u"\n".join([u"Es gibt keinen Markt in %s. Füge ihn doch hinzu!",
                                  u"https://github.com/wo-ist-markt/wo-ist-markt.github.io"
                                 ])
            outputs.append([data['channel'], message % location.lower()])

    if data['text'] == "Wo gibts Markt?":
        message = u"Es gibt Märkte in %s"
        markets = ", ".join(SUPPORTED_CITIES)
        combined = message % markets
        outputs.append([data['channel'], combined])

    open_markets = match_text(data['text'])
    if open_markets is not None:
        outputs.append([data['channel'], open_markets])


