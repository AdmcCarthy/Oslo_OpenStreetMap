#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Completed for Udacity
Data Analyst nano-degree.
"""

import os
from unscramble import (
    dataset,
    resample
    )

import bz2

def main():
    """Investigate the Oslo
    OpenStreetMap dataset.
    """

    test = False

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
    filepath = filepath

    if test:
        # Reduce the number of elements to speed up testing
        resample.sample(filepath, "sample.osm")
        filepath = "sample.osm"

if __name__ == '__main__':
    main()
