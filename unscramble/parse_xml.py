#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint


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


def attribute_compare(file):
    """Define regular expressions
    then make a dictionary of how many
    issues there are for each condition
    specified.
    """

    lower = re.compile(r'^([a-z]|_)*$')
    lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
    problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

    def key_type(element, keys):
        if element.tag == "tag":
            val = element.attrib["k"]
            
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

    process_map(file)

def audit(filename):
    """Parse
    """

    constraint = "tag"

    for event, elem in ET.iterparse(filename, events=("start",)):
        if elem.tag == "way":
            # Only returns those that are named constraint
            for tag in elem.iter(constraint):