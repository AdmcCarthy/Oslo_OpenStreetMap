#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict


def count_tags(filename):
    """Take a count of all tags
    within an XML file.

    Returns a dictionary showing all
    tags and how often they occur.
    """

    file_overview = {}
    for event, elem in ET.iterparse(filename):
        key = elem.tag
        if key not in file_overview:
            file_overview[key] = 1
        else:
            file_overview[key] += 1

    return file_overview


def attribute_compare(file, tag_v, attribute):
    """Define regular expressions
    then make a dictionary of how many
    issues there are for each condition
    specified.
    """

    lower = re.compile(r'^([a-z]|_)*$')
    lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
    problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

    def key_type(element, keys):
        if element.tag == tag_v:
            val = element.attrib[attribute]

            if lower.search(val):
                keys["lower"] += 1
            elif lower_colon.search(val):
                keys["lower_colon"] += 1
            elif problemchars.search(val):
                keys["problemchars"] += 1
            else:
                keys["other"] += 1

        return keys

    def process_map(filename):
        keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
        for _, element in ET.iterparse(filename):
            keys = key_type(element, keys)

        return keys

    key = process_map(file)

    return key


def get_unique(file, attribute):
    """Count the number of
    unique values in an attribute.
    """

    def get_user(element):
        d = element.attrib
        if attribute in d:
            name = element.attrib[attribute]
            return name


    def process_map(filename):
        users = set()
        for _, element in ET.iterparse(filename):
            name = get_user(element)
            users.add(name)

        users.remove(None)
        return users


    user = process_map(file)
    return user


def way_name(filename):
    """Identify inccorect ends to
    way names.

    Correct these based on mapping.
    """

    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


    expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
                "Trail", "Parkway", "Commons"]


    mapping = { "St": "Street",
                "St.": "Street",
                "Ave" : "Avenue",
                "Ave." : "Avenue",
                "Rd." : "Road",
                "Rd" : "Road"
                }


    def audit_street_type(street_types, street_name):
        m = street_type_re.search(street_name)
        if m:
            street_type = m.group()
            if street_type not in expected:
                street_types[street_type].add(street_name)


    def is_street_name(elem):
        return (elem.attrib['k'] == "addr:street")


    def audit(osmfile):
        osm_file = open(osmfile, "r", encoding='utf8')
        street_types = defaultdict(set)
        for event, elem in ET.iterparse(osm_file, events=("start",)):

            if elem.tag == "node" or elem.tag == "way":
                for tag in elem.iter("tag"):
                    if is_street_name(tag):
                        audit_street_type(street_types, tag.attrib['v'])
        osm_file.close()
        return street_types


    def update_name(name, mapping):

        street = street_type_re.search(name)

        if street:
            print(street)
            replacement = mapping[street.group()]
            name = street_type_re.sub(replacement, name)

        return name


    new_names = []
    st_types = audit(filename)

    # pprint.pprint(dict(st_types))

    for st_type, ways in st_types.items():
        for name in ways:
            better_name = update_name(name, mapping)

            new_names.append(better_name)

    return new_names
       