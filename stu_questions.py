
"""
    stu_questions.py

    It contains every operations on questions
"""

import csv
import stu_misc
from math import sqrt


QUESTION_TAGS   = 'data/question_tags.csv'
QUESTION_SAMPLE = 'data/sample_questionsv0.csv'

# private functions

def _load_questions():
    print('Load questions from database...')
    with open(QUESTION_SAMPLE) as f:
        f.readline()            # Ignore the first line
        reader = csv.reader(f.readlines(), skipinitialspace=True)
        qarray = []
        for r in reader:
            qarray.append( (int(r[0]), stu_misc.concatenate(r[5], r[6])) )
        print('Done')
        return qarray

# public functions
def get_question_from(tagname):
    """
        Return the list of the questions that are related to the tags

        Arg:
            the name of the tag
        Return:
            the list of question identifier.
            Each identifier refers to an existing question in the sample
    """
    qarray = []
    with open(QUESTION_TAGS, 'r') as f:
        f.readline()    # I ignore this first line because it's just metadata
        for line in f:
            row = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            qidv = int(row[0])
            if row[1] == tagname and qidv >= stu_misc.MIN_ID and qidv <= stu_misc.MAX_ID and (qidv % 10) == 0:
                qarray.append(qidv)
            elif qidv > stu_misc.MAX_ID:
                break
    return filter(qarray)

def is_valid(qid):
    """
        Check if the identifier is valid, i.e. if the question
        this ID refers to exists in the sample of questions

        I used the dichotomic search because every questions in the sample
        are sorted by there identifier

        Arg:
            the question identifier

        Return:
            True if it is in the sample, False otherwise
    """
    return stu_misc.dichotomic_search([q[0] for q in questions], qid)

def filter(qarray):
    """
        Filter the array of question identifiers.
        It generates a new array that contains the identifiers
        that refers to the questions in the sample

        Arg:
            an array of questions

        Return:
            the filtered array
    """
    return [q for q in qarray if is_valid(q)]

def get_documents(idqarray):
    """
        Retrieve the documents according to their identifiers

        Arg:
            the list of identifiers
        Return:
            the list of documents (the questions)
    """
    documents = []
    qids = [q[0] for q in questions]
    for id in idqarray:
        qindex = stu_misc.dichotomic_find(qids, id)
        if qindex is not None:
            documents.append(questions[qindex][1])
    return documents

# Global variable
questions = _load_questions()

"""
    Test
"""

#print(len(questions))
#print(questions[0])
"""
print('Questions from c++')
qs = get_question_from('c++')
print('number of questions')
print(len(qs))
print('check')
print(all(q >= stu_misc.MIN_ID and q <= stu_misc.MAX_ID and (q % 10) == 0 for q in qs))
print('get documents')
qdoc = get_documents(qs)
print(len(qdoc))
print(filter([75,76,77,78,79,80, 330, 331, 332]))
"""
