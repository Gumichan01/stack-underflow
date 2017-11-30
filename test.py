
import csv
from stu_tags import *
from stu_questions import *

#reader = csv.reader(['1997,Ford,E350,"Super, luxurious truck"'], skipinitialspace=True)
#for r in reader:
#    print(r)
"""
with open('data/sample_questions.csv') as csvf:
    reader = csv.reader(csvf, skipinitialspace=True)
    for r in reader:
        #r[6] = ''.join(' ' if c == '\n' or c == '\t' else c for c in r[6])
        #print(len(r))
        print(r[0])
    print(v)
"""

print('Tags')
tgs = getTagsOfCluster(1)
print(tgs)
q = getQuestions(tgs[1])
print(len(q))
s = ''
print('get the question no. ', q[0])
with open('data/sample_questions.csv') as csvf:
    reader = csv.reader(csvf, skipinitialspace=True)
    for r in reader:
        if r[0] == 'Id':
            continue
        r[6] = ''.join(' ' if c == '\n' or c == '\t' else c for c in r[6])
        if int(r[0]) == q[0]:
            s = ''.join(r[5], r[6])

print()
print(s)
