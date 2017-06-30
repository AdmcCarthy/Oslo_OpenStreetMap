#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Get dataset required for this
investigation.
"""

from __future__ import print_function
from urllib import request
import os
from bz2file import BZ2File
import bz2

def get_data(dirpath):
    """Download the oslo OpenStreetMap
    dataset and uncompress.

    Store it in the folder above the
    repository.
    """

    storepath = os.path.abspath(os.path.join(dirpath, "..", "oslo_norway.osm"))

    if os.path.isfile(storepath):
        print('Data is present')
        print("")
    else:
        print('Starting download')
        print('File is approx 96 MB, this may take while....')
        # Get compressed osm dataset
        url = "https://s3.amazonaws.com/metro-extracts.mapzen.com/oslo_norway.osm.bz2"

        # Store one folder up so the data in not included in repository.
        request.urlretrieve(url, filename=storepath)

        print('Data downloaded')

def decompress(filepath):
    """Decompress the bz2 file
    type.

    Not operational yet!!!

    Would be better to have this within
    the code but appears there is some
    issue as the file is a multistream
    file.
    """

    zipfile = filepath

    with BZ2File(zipfile, 'rb') as zf:
        bz2.decompress(zf)
        print('Data decompressed')
