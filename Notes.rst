================
Notes on problem
================

-------------
Data Elements
-------------

See OSM wiki for more.

http://wiki.openstreetmap.org/wiki/Elements

The three key elements are.

nodes - (defining points in space)
ways - (defining linear features and area boundaries)
relations - (sometimes used to explain how other elements work together)

All of the above can have tags which describe the meaning of a particular element.



-------
OSM XML
-------

See OSM wiki for more information.

http://wiki.openstreetmap.org/wiki/OSM_XML

OSM XML files are constructed out of OSM data primitives.

The top of the file will include an XML suffix and osm version as an element.

        output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output.write('<osm>\n  ')

bounds will cover the area coverage of the XML (not always present)

Following this the main component of the file will consist
of three blocks.

Nodes, which contain location. These will include tags of each node.

Ways. These include the reference to it's nodes for each way. The tags of each way.

Relations. References to its members for each relatin. The tags of each relation.

