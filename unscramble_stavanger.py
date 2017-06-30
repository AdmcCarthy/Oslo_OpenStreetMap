#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from unscramble import resample

def main():

    dir = os.path.dirname(__file__)
    osm_file = os.path.join(dir, '/data/map_stavanger.osm')

    resample.sample(osm_file, "sample.osm")

if __name__ == '__main__':
    main()
