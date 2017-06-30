=======================
Stavanger_OpenStreetMap
=======================

Exploring data for Stavanger in Open Street Map

--------
Workflow
--------

Parse XML file

Unravel the dataset

Identify problems in the data

Audit and clean the data

Import cleaned version in database

Explore database to identify interesting features

-------
Dataset
-------

Data is taken from OpenStreetMap.org using the Overpass API.

https://www.openstreetmap.org/export#map=13/58.9611/5.6777

Overpass QL version of this reques would be:

    (
        node(58.9976,5.6262,58.9245,5.7292);
        <;
    );
    out meta;

The data islicensed under the Open Data Commons Open Database License (ODbL)
by the OpenStreetMap Foundation (OSMF).

https://www.openstreetmap.org/copyright

---------
Resources
---------

^^^^^^^^^^^^^
OpenStreetMap
^^^^^^^^^^^^^

https://wiki.openstreetmap.org/wiki/Main_Page

http://wiki.openstreetmap.org/wiki/OSM_XML

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Hitchkiker's Guide to Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

http://docs.python-guide.org/en/latest/scenarios/db/

http://docs.python-guide.org/en/latest/scenarios/xml/

