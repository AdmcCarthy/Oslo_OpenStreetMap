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
