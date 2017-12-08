
"""
    stu_questions.py

    It contains every operations on questions
"""

import csv
import stu_misc

from stu_tags import *
from math import sqrt


QUESTION_TAGS   = 'data/question_tags.csv'
QUESTION_SAMPLE = 'data/sample_questionsv0.csv'

def getQTags(question_id):
    """
        Return a list of tags related the question specified by its id

        Arg:
            question_id
        Return:
            the list of tags if found, None otherwise
    """
    qtags = []
    with open(QUESTION_TAGS, 'r') as f:
        f.readline()    # I ignore this first line because it's just metadata
        for line in f:
            row = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            qid = int(row[0])
            if qid == question_id:
                tags.append(row[1])
            elif qid > question_id:
                return qtags if qtags != [] else None
        return qtags if qtags != [] else None

def getQuestionsFromTag(tagname):
    """
        Return the list of the questions that are related to the tags

        Arg:
            the name of the tag
        Return:
            the list of question, by identifier
    """
    qarray = []
    with open(QUESTION_TAGS, 'r') as f:
        f.readline()    # I ignore this first line because it's just metadata
        for line in f:
            row = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            qidv = int(row[0])
            if row[1] == tagname and isInSample(qidv):
                qarray.append(qidv)
    return qarray

def isInSample(qid):
    """
        Return the list of question identifers
        so that each identifier refers to a real question in the sample

        Arg:
            the question identifier

        Return:
            True if it is in the sample, False otherwise
    """
    with open(QUESTION_SAMPLE, 'r') as csvf:
        reader = csv.reader(csvf, skipinitialspace=True)
        for r in reader:
            if r[0] == 'Id' or int(r[0]) < qid:
                continue
            else:
                return int(r[0]) == qid

def filterQuestions(qarray):
    """
        Filter the array of question. It generates a new array that contains
        the identifiers tha refers to the questions in the sample

        Arg:
            an array of questions

        Return:
            the filtered array
    """
    return [q for q in qarray if isInSample(q)]

"""
    Test
"""

#print('Questions from c++')
#qs = getQuestionsFromTag('c++')
#print(len(getQuestionsFromTag('c++')))
#print(filterQuestions([75,76,77,78,79,80, 330, 331, 332]))
