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

def std_deviation(lst):
    return sqrt(variance(lst))


def stats_questions():
    """
        Preprocessing function that generates basics statistics about
        the score of the questions posted on stack Overflow from questions.csv.

        return: a n-tuple (min_score, max_score, average_score, variance, standard deviation)

        note: You need to call this function once
    """
    vmin   = 0
    vmax   = 0
    vtotal = 0
    n      = 0
    vtotal_sq = 0
    with open('data/questions.csv','r') as f:
        f.readline()    # I ignore the 1st line because is just metadata
        for line in f:
            v = int(line.strip('\n').split(',')[4])
            vmin = v if v < vmin else vmin
            vmax = v if v > vmax else vmax
            vtotal += v
            # Variance
            n += 1
            vtotal_sq += v ** 2
        avg = (vtotal / n)
        variance = ((1 / n) * vtotal_sq) - (avg ** 2)
        return (vmin, vmax, avg, variance, sqrt(variance))

def write_stats_in(stat, filename):
    with open(filename, "w+") as f:
        metadata = 'min, max, average, variance, standard deviation\n'
        s = str(stat).strip('()') + '\n'
        f.write(metadata)
        f.write(s)

# Global variables
#qstats = stats_questions()
tags = loadTags('data/Tags.xml')

"""
    Test
"""
#print(countTags())
#print(getTagInfoByName("java"))
#print(getTagID("java"))
#print(getTagName(17))
#print(str((0, 20, 15, 4, 2)).strip('()') )
#write_stats_in((0, 20, 15, 4, 2), 'question_score_stats.csv')
"""
    Real code
"""
#print(qstats)
#write_stats_in(stats_questions(), 'question_score_stats.csv')