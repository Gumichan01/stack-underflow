#!/bin/python3

import xml.etree.ElementTree as xmlt;
from collections import namedtuple as struct

"""
Tag is a structure (named tuple) that contains information about a tag
"""
Tag = struct("Tags", "id name postid wikipid")

# "private" functions
#note use d.get(key, default=None)
# FIXME
def dictToTag(d):
    """
        Convert the attibutes of a children to a names tag
        param: d the dictionary gicevn by getTagInfo
        return tha named structure Tag
    """
    return Tag(id = d.get["Id"], name = d["TagName"],
               postid  = (d["ExcerptPostId"] if d["ExcerptPostId"] is not None else None),
               wikipid = (d["WikiPostId"] if d["WikiPostId"] is not None else None))

def loadTags(file):
    root = xmlt.parse(file).getroot()
    tset = set()
    for child in root:
        print(child.attrib)
        tset.add(dictToTag(child.attrib))
    return tset

# Variables
tags = loadTags('data/Tags.xml')


def countTags():
    """
    Count the number of tags in data/Tags.xml
    return: the number of tags
    """
    return len(tags)

# Is there a possibility to merge those functions in one?
def getTagInfoByName(tagname):
    """
    Get information about a tag specified by its name
    param: tagname the tag
    return: named n-tuple Tags is found, None otherwise
    """
    for t in tags:
        if t.name == tagname:
            return t
    # not found
    return None

def getTagInfoByID(idtag):
    """
    Get information about a tag specified by its ID
    param: idtag the tag
    return: named n-tuple Tags is found, None otherwise
    """
    for t in tags:
        if t.id == idtag:
            return t
    # not found
    return None

def getTagName(idtag):
    """
    Get the name of the tag according to its id
    return: the name of the tag if found, None otherwise
    """
    tag = getTagInfoByID(idtag);
    return tag.name if tag is not None else None


def getTagID(tagname):
    """
    Get the ID of the tag according to its name
    return: the name of the tag if found, None otherwise
    """
    tag = getTagInfoByName(tagname);
    return tag.id if tag is not None else None



# Test
print(countTags())
#print(getTagInfoByName("java"))
#print(getTagID("java"))
#print(getTagName("utfcpp"))
