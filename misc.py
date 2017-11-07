#!/bin/python3

from math import sqrt
import xml.etree.ElementTree as xmlt
from collections import namedtuple as struct

"""
    Stack Overflow - tags
"""

# Tag is a structure (named tuple) that contains information about a tag
Tag = struct("Tags", "id name postid wikipid")

# "private" functions
def dictToTag(d):
    """
        Convert the attibutes of a children to a names tag
        param: d the dictionary gicevn by getTagInfo
        return the named structure Tag
    """
    vid      = d.get("Id")
    vpostid  = d.get("ExcerptPostId")
    vwikipid = d.get("WikiPostId")
    id       = int(vid) if vid is not None else None
    postid   = int(vpostid) if vpostid is not None else None
    wikipid  = int(vwikipid) if vwikipid is not None else None
    return Tag(id = id, name = d.get("TagName"), postid = postid, wikipid = wikipid)

def loadTags(file):
    root = xmlt.parse(file).getroot()
    tset = set()
    for child in root:
        tset.add(dictToTag(child.attrib))
    return tset

# Variables
tags = loadTags('data/Tags.xml')

# "public" functions
def countTags():
    """
    Count the number of tags in data/Tags.xml
    return: the number of tags
    """
    return len(tags)

# Is there a possibility to merge these functions in one?
def getTagInfoByName(tagname):
    """
    Get information about a tag specified by its name
    param: tagname the tag
    return: named n-tuple Tags is found, None otherwise
    """
    for t in tags:
        if t.name == tagname:
            return t
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

"""
    Stack Overflow - statistics about questions
"""

def average(lst):
    return (sum(lst) / len(lst))

def median(lst):
    lst.sort()
    return(lst[len(lst)//2])

def variance(lst):
    moy = average(lst)
    d = [(item - moy) ** 2 for item in lst]
    return (1/ (len(lst)-1)) * sum(d)

def ecarttype(lst):
    return sqrt(variance(lst))

def stats_questions():
    with open('data/Tags.xml') as f:
        pass
    pass

# Variable "globale"
qstats = stats_questions()

"""
    Test
"""
print(countTags())
print(getTagInfoByName("java"))
print(getTagID("java"))
print(getTagName(17))
print(qstats)
