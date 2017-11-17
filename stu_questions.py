
"""
    stu_questions.py

    It contains every operations on questions
"""

import stu_tags

from math import sqrt

QUESTION_TAGS = 'data/question_tags.csv'

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


def getQTags(question_id):
    """
        Return a list of tags related the question specified by its id

        Arg:
            question_id
        Return:
            the list of tags if found, None otherwise
    """
    had_found_qid = False
    tags = []
    with open(QUESTION_TAGS, 'r') as f:
        f.readline()    # I ignore this first line because it's just metadata
        for line in f:
            row = line.strip('\n').split(',')
            qid = row[0]
            if question_id == qid:
                if not(had_found_qid):
                    had_found_qid = True
                tags.append(row[1])
            else:
                if had_found_qid:
                    return tags
    return None

print(getQTags(25))
