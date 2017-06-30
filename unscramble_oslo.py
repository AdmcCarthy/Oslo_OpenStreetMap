#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Completed for Udacity
Data Analyst nano-degree.BrokenPipeError
"""

import os
from unscramble import (
    dataset,
    resample
    )

def main():
    """Investigate the Oslo
    OpenStreetMap dataset.
    """

    # Download and uncompress the dataset
    # data stored in folder above repository
    dataset.get_data()

    dirpath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(dirpath, "..", "oslo_norway.osm"))

    #resample.sample(filepath, "sample.osm")

if __name__ == '__main__':
    main()
