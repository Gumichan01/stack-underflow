
import csv
#from stu_tags import *
#from stu_questions import *

"""
reader = csv.reader(['ID,NAME,TEXT', '1,jello,gumi', '2,shdsdbkzd,jzfkzj'], skipinitialspace=True)
for r in reader:
    print(r)
"""

def generate_string_from(array):
    return ' '.join([w for w in array])

def save(pairs):
    with open('dict.csv','w+') as f:
        #f.write('tag, words\n')
        for t, wl in pairs:
            f.write(t)
            f.write(', ')
            f.write(generate_string_from(wl))
            f.write('\n')


l = ['hello','world','gumi', 'chan']

print(generate_string_from(l))
save([('c++', l), ('java', l), ('python', l), ('machine-learning', l)])

# another experiment

#
"""
def isSorted():
    with open('data/sample_questionsv0.csv') as csvf:
        v = 0
        qid = 0
        qidp = 0
        reader = csv.reader(csvf, skipinitialspace=True)
        for r in reader:
            if r[0] == 'Id':
                continue

            qid = int(r[0])
            if v == 0 or qidp <= qid:
                qidp = qid
                v += 1
            elif qid < qidp:
                    return False
        return True
"""

# nothing

"""
with open('data/sample_questionsv0.csv', 'r') as csvf:
    reader = csv.reader(csvf, skipinitialspace=True)
    for r in reader:
        print(r[0])
"""
