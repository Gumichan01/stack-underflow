#!/bin/python3

from math import sqrt
from collections import namedtuple as struct

"""
    Stack Overflow - tags
"""

# constant values
TAGS_FILE         = 'data/sample_tags.csv'
TAG_NETWORK_NODE  = 'data/stack_network_nodes.csv'
TAG_NETWORK_LINKS = 'data/stack_network_links.csv'

# Tag is a structure (named tuple) that contains information about a tag
Tag = struct("TagInfo", "id name")

# "private" functions
def _loadTags():
    """
        It loads the tags from TAGS_FILE and and stores them
        in a data structure that contains the tags

        Return:
            an iterable data structure that contains the tags on success, None
    """
    with open(TAGS_FILE) as f:
        f.readline()    # I ignore the first line
        tarray = []
        lines  = f.readlines()
        for line in lines:
            row = line.strip('\n')
            tarray.append(Tag(id = int(row[0]), name = row[1]))
        return tarray

# "public" functions
def countTags():
    """
        Count the number of tags

        Return:
            the number of tags
    """
    return _taglength

# Is there a possibility to merge these functions in one?
def getTagInfoByName(tagname):
    """
        Get information about a tag specified by its name

        Arg:
            tagname the tag

        Return:
            a named n-tuple TagInfo is found, None otherwise
    """
    for t in tags:
        if t.name == tagname:
            return t
    return None

def getTagInfoByID(idtag):
    """
        Get information about a tag specified by its ID

        Arg:
            the tag, specified by the identifier

        Return:
            a named n-tuple TagInfo is found, None otherwise
    """
    for t in tags:
        if t.id == idtag:
            return t
    return None

def getTagName(idtag):
    """
        Get the name of the tag according to its id

        Return:
            the name of the tag if found, None otherwise
    """
    tag = getTagInfoByID(idtag);
    return tag.name if tag is not None else None


def getTagID(tagname):
    """
        Get the ID of the tag according to its name

        Return:
            the name of the tag if found, None otherwise
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
    return getTagClusterByName(tag_name) if tag_name is not None else None

    """
    with open(TAG_NETWORK_NODE, 'r') as f:
            f.readline()    # I ignore the first because it's just metadata
            for line in f:
                row = line.strip('\n').split(',')
                tname = row[0]
                if tag_name == tname:
                    return int(row[1])
    return None
    """

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
tags = _loadTags()
_taglength = len(tags)

"""
    Test
"""
print(countTags())
#print(getTagInfoByName('java'))
#print(getTagID('java'))
#print(getTagName(17))
#print(getTagClusterByID(17))
#print(getTagClusterByID(getTagID('java')))
#print(getTagClusterByName('java'))
#print(getTagClusterByName(getTagName(17)))
#print(getTagsOfCluster(5))
#print(getTagsOfCluster(getTagClusterByName(getTagName(17))))
#print(getTagsOfCluster(getTagClusterByID(getTagID('java'))))

"""
# get the tags from a cluster
for i in range(100):
    t = getTagsOfCluster(i)
    if t is not None:
        print(i, t)
"""
