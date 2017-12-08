
"""
    stu_questions.py

    It contains every operations on questions
"""

from stu_tags import *
from math import sqrt
import stu_misc

QUESTION_TAGS = 'data/question_tags.csv'
SAMPLE_QUESTIONS = 'data/sample_questionsv0.csv'

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
            if row[1] == tagname:
                qarray.append(int(row[0]))
    return qarray

"""
    Test
"""

print('Questions from c++')
qs = getQuestionsFromTag('c++')
print(len(qs))
