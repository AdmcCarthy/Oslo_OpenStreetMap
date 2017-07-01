#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Completed for Udacity
Data Analyst nano-degree.
"""

import os
from unscramble import (
    dataset,
    resample,
    xml_split
    )

import bz2

def main():
    """Investigate the Oslo
    OpenStreetMap dataset.
    """

    test = True

    dirpath = os.path.dirname(__file__)

    # Download the dataset
    # data stored in folder above repository
    dataset.get_data(dirpath)

    filepath = os.path.abspath(os.path.join(dirpath, "..", "oslo_norway"))

    # File is in a bz2 during download
    # !!! Currently no method to decompress a
    # multi-stream bz2 file has been found.
    # dataset.decompress(filepath)

    # Please manually decompress the file and continue
    # e.g. 7Zip for windows
    #
    # Modify the filepath if required.

    if test:
        filepath = os.path.abspath(os.path.join(dirpath, "..", "stav"))

if __name__ == '__main__':
    main()
