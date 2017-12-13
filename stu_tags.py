#!/bin/python3

"""
    Stack Overflow - tags
"""

from math import sqrt
from collections import namedtuple as struct
import stu_misc

# constant values
#files
TAGS_FILE         = 'data/sample_tags.csv'
TAG_NETWORK_NODE  = 'data/stack_network_nodes.csv'
#TAG_NETWORK_LINKS = 'data/stack_network_links.csv'

# "private" functions
def _load_tags():
    """
        It loads the tags from TAGS_FILE and and stores them
        in a data structure that contains the tags

        Return:
            an iterable data structure that contains the tags on success, None
    """
    with open(TAGS_FILE) as f:
        f.readline()    # I ignore the first line
        tarray = []
        dic = dict()
        lines = f.readlines()
        for line in lines:
            row  = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            name = row[1]
            if name not in dic:
                tarray.append(name)
                dic[name] = 0
        return tarray

# "public" functions
# cluster
def get_tag_cluster(tag_name):
    """
        Return the cluster of the tag

        Arg:
            the tag specified by its name
        Return:
            the tag cluster (identifier) if found, None otherwise
    """
    with open(TAG_NETWORK_NODE, 'r') as f:
            f.readline()    # I ignore the first line because it's just metadata
            for line in f:
                row = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
                tname = row[0]
                if tag_name == tname:
                    return int(row[1])
    return None
"""
def getTagsOfCluster(cluster_id):
        Return the tags contained in a cluster specified by its iD

        Arg:
            the ID of the cluster
        Return:
            the tags that belong to the cluster, None otherwise
    with open(TAG_NETWORK_NODE, 'r') as f:
        cluster_tags = []
        f.readline()    # I ignore the first line because it's just metadata
        for line in f:
            row = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            cluster_value = int(row[1])
            if cluster_value == cluster_id:
                cluster_tags.append(row[0])
        return cluster_tags if cluster_tags != [] else None
"""

# Global variables
tags = _load_tags()

"""
    Test
"""
#print(len(tags))
#print(get_tag_cluster('c++'))
#print(tags[0])
#print(tags[79])
