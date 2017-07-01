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

^^^^
Node
^^^^

Represents a point in latitude and longitude.

Minimum is an id number and pair of coordinates.

Nodes can be used to define th shape of a way.

^^^
Way
^^^

A way a list of nodes that define a polyline.

This can be used for linear features or boundaries.

^^^^^^^^
Relation
^^^^^^^^

A multi-purpose data structure that documents a relationship between two or more data elements.

nodes, ways and other relations can exist as members within a relation.

Elements can also have a role within the relation.

^^^
Tag
^^^

Describe the meaning of the particular element.

Will occur with a key, value pair.

Nodes are often untagged if they are part of ways.

Nodes and ways can be untagged if they are members of a relation.

^^^^^^^^^^^^^^^^^
Common attributes
^^^^^^^^^^^^^^^^^

id, user, uid, timestamp, visible, version, changeset

See OpenStreetMap wiki for a detailed list of map feature attributes.

http://wiki.openstreetmap.org/wiki/Map_Features

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

