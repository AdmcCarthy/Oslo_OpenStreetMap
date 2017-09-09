#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unscramble OSM data.

Parse through then asses data from open street maps.
"""

import os
import pprint
from unscramble import (
    dataset,
    parse_xml,
    )


def main():
    """Investigate the Oslo
    OpenStreetMap dataset.
    """

    test = True

    dirpath = os.path.dirname(__file__)

    # Download the dataset
    # data stored in folder above repository
    dataset.get_data(dirpath)

    filepath = os.path.abspath(os.path.join(dirpath, "..", "oslo_norway.osm"))

    # File is in a bz2 during download
    # !!! Currently no method to decompress a
    # multi-stream bz2 file has been found.
    # dataset.decompress(filepath)

    # Please manually decompress the file and continue
    # e.g. 7Zip for windows
    #
    # Modify the filepath if required.

    if test:
        filepath = os.path.abspath(os.path.join(dirpath, "..", "stav.osm"))

    # Count frequency of tags in the xml file
    tags = parse_xml.count_tags(filepath)

    print("tags present in dataset")
    pprint.pprint(tags)

    issues = parse_xml.attribute_compare(filepath, "tag", "k")

    print("issues")
    pprint.pprint(issues)

    users = parse_xml.get_unique(filepath, "user")
    print("unique users")
    pprint.pprint(users)

    # new_names = parse_xml.way_name(filepath)
    # pprint.pprint(new_names)

if __name__ == '__main__':
    main()
