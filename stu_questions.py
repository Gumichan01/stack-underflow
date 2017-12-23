
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
        qdict = dict()
        for r in reader:
            qdict[int(r[0])] = stu_misc.concatenate(r[5], r[6])
        print('Done')
        return qdict

# load the lookup table from the original lookup file (heavy operation)
def _load_lookup_heavy():
    print('Load lookup table from ',QUESTION_TAGS,'...')
    ldict = dict()
    with open(QUESTION_TAGS, 'r') as f:
        f.readline()    # I ignore this first line because it's just metadata
        for line in f:
            row = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            qidv = int(row[0])
            tgname = row[1]
            # A new tag
            if ldict.get(tgname) is None:
                ldict[tgname] = []

            # Add the identifier of the question in the tag
            if qidv >= stu_misc.MIN_ID and qidv <= stu_misc.MAX_ID and (qidv % 10) == 0 and is_valid(qidv):
                ldict[tgname].append(qidv)
    print('Done')
    return ldict


def _load_lookup():
    with open('lookup.csv','r') as f:
        print('Load generated lookup table...')
        ldict = dict()
        for line in f.readlines():
            row  = line.strip(stu_misc.ENDL).split(stu_misc.COMMA)
            ldict[row[0]] = [int(v) for v in row[1].split(' ')]
        print('Done')
    return ldict


# public functions
def _get_question_from(tagname):
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
    return questions.get(qid) is not None

def _filter(qarray):
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
    if idqarray == []:
        return []

    documents = []
    #qids = [q[0] for q in questions]
    for id in idqarray:
        #qindex = stu_misc.dichotomic_find(qids, id)
        if questions.get(id) is not None:
            documents.append(questions[id])
    return documents

# Global variable
questions = _load_questions()
lookup_table = _load_lookup()
"""
print('Save lookup')
with open('lookup.csv', 'w+') as f:
    for t in lookup_table:
        if lookup_table[t] == []:
            continue

        f.write(t)
        f.write(',')
        f.write(' '.join([str(w) for w in lookup_table[t]]))
        f.write('\n')

print('Lookup saved')
"""

"""
    Test
"""

#print(len(questions))
#print(len(lookup_table))
#print('Questions from c++')
#print('number of questions')
#print(len(lookup_table['c++']))
#print('get documents')
#qdoc = get_documents(lookup_table['c++'])
#print(len(qdoc))
