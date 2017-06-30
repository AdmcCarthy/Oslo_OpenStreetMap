#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get dataset required for this
investigation.
"""

from __future__ import print_function
from urllib import request
import os

def get_data():
    """Download the oslo OpenStreetMap
    dataset and uncompress.

    Store it in the folder above the
    repository.
    """

    os.chdir("..")
    if not os.path.isdir('test'):

        print('Starting download')
        print('File is approx 96 MB, this may take while....')
        # Get compressed osm dataset
        url = "https://s3.amazonaws.com/metro-extracts.mapzen.com/oslo_norway.osm.bz2"
        request.urlretrieve(url, filename='oslo_norway.osm')

        print('Data downloaded')
