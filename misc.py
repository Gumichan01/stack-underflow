#!/bin/python3

import xml.etree.ElementTree as xmlt;


def countTags():
    """
    Count the number of tags in data/Tags.xml
    return: the number of tags
    """
    tree = xmlt.parse('data/Tags.xml');
    return len(tree.getroot().getchildren());


print(countTags());
