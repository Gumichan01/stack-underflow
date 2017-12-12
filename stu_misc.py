#!/bin/python3

"""
    stu_misc.py is a file that contains miscellaneous functions
"""

import re
from math import sqrt

# miscellaneous constant values

# delimiters
ENDL  = '\n'
COMMA = ','

# Question identifers
MIN_ID = 80
MAX_ID = 4714870

# dictionary
DICT_FILE='dict.csv'

# miscellaneous functions

def concatenate(first_string, second_string):
    """
        Generate a document that contains the label + the content of a question
        and format it

        Arg:
            Two strings to concatenate

        Return:
            the formatted document
    """
    # I want to consider a label + the content of the question as a document
    concat = ''.join([first_string, ' ', second_string])
    nosep  = ''.join('' if c == '\n' or c == '\t' else c for c in concat)
    # Since a question is written in HTML format, I have to get rid of html flags
    # and every punctuations
    nothml = re.sub('<[a-zA-Z][^>]*>|</[a-zA-Z]+>', '', nosep)
    substr = re.sub('['+string.punctuation+']', ' ', nothml)
    # At this point, my document has several spaces between worlds, I reduce them to one
    return re.sub(' +', ' ', substr).rstrip(' ').lower()


def dichotomic_search(l,v):
    """
        Try to find the a value in a sorted list of elements

        Arg:
            the list where you want to search and v
        Result:
            True if found, False otherwise
    """
    begin = 0
    end = len(l) -1
    found = False

    while not(found) and begin <= end:
        indexm = (begin + end) // 2
        if l[indexm] == v:
            found = True
        else:
            if v > l[indexm]:
                begin = indexm + 1
            else:
                end   = indexm - 1
    return found

def dichotomic_find(l,v):
    """
        Try to find the a value in a sorted list of elements

        Arg:
            the list where you want to search and v
        Result:
            the content if found, None otherwise
    """
    indexm = None
    begin = 0
    end = len(l) -1
    found = False

    while not(found) and begin <= end:
        indexm = (begin + end) // 2
        if l[indexm] == v:
            found = True
        else:
            if v > l[indexm]:
                begin = indexm + 1
            else:
                end   = indexm - 1
    return indexm if found else None

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


"""
    Test
"""
#lst = [16,21,32,4,56,64,7,80,96,42,1024]
#print(average(lst))
#print(median(lst))
#print(variance(lst))
#print(std_deviation(lst))
