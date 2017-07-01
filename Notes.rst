================
Notes on problem
================

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

