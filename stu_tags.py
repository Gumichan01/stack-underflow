#!/bin/python3

"""
    misc.py is a file that contains miscellaneous functions
    and make preprocessing of data
"""

from math import sqrt
import xml.etree.ElementTree as xmlt
from collections import namedtuple as struct

"""
    Stack Overflow - tags
"""

# constant values
TAGS_FILE         = 'data/Tags.xml'
TAG_NETWORK_NODE  = 'data/stack_network_nodes.csv'
TAG_NETWORK_LINKS = 'data/stack_network_links.csv'

# Tag is a structure (named tuple) that contains information about a tag
Tag = struct("Tags", "id name postid wikipid")

# "private" functions
def _dictToTag(d):
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

def _loadTags(file):
    root = xmlt.parse(file).getroot()
    tset = set()
    for child in root:
        tset.add(_dictToTag(child.attrib))
    return tset

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


#cluster

def getTagClusterByID(tag_id):
    """
        Return the tag cluster of the tag

        Arg:
            the tag specified by its id
        Return:
            the tag cluster (identifier) if found, None otherwise
    """
    tag_name = getTagName(tag_id)
    with open(TAG_NETWORK_NODE, 'r') as f:
            f.readline()    # I ignore the first because it's just metadata
            for line in f:
                row = line.strip('\n').split(',')
                tname = row[0]
                if tag_name == tname:
                    return int(row[1])
    return None

def getTagClusterByName(tag_name):
    """
        Return the tag cluster of the tag

        Arg:
            the tag specified by its name
        Return:
            the tag cluster (identifier) if found, None otherwise
    """
    with open(TAG_NETWORK_NODE, 'r') as f:
            f.readline()    # I ignore the first because it's just metadata
            for line in f:
                row = line.strip('\n').split(',')
                tname = row[0]
                if tag_name == tname:
                    return int(row[1])
    return None

def getTagsOfCluster(cluster_id):
    """
        Return the tags conained in a cluster specified by its iD

        Arg:
            the ID of the cluster
        Return:
            the tags that belong to the cluster, None otherwise
    """
    with open(TAG_NETWORK_NODE, 'r') as f:
        cluster_tags = []
        f.readline()    # I ignore the first because it's just metadata
        for line in f:
            row = line.strip('\n').split(',')
            cluster_value = int(row[1])
            if cluster_value == cluster_id:
                cluster_tags.append(row[0])
        return cluster_tags if cluster_tags != [] else None


# Global variables
tags = _loadTags(TAGS_FILE)

"""
    Test
"""
#print(countTags())
#print(getTagInfoByName("java"))
#print(getTagID("java"))
#print(getTagName(17))
#print(getTagClusterByID(17))
#print(getTagClusterByID(getTagID("java")))
#print(getTagClusterByName('java'))
#print(getTagClusterByName(getTagName(17)))
#print(getTagsOfCluster(5))
#print(getTagsOfCluster(getTagClusterByName(getTagName(17))))
#print(getTagsOfCluster(getTagClusterByID(getTagID("java"))))

"""
for i in range(100):
    t = getTagsOfCluster(i)
    if t is not None:
        print(i, t)
"""
