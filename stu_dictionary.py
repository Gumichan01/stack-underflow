
"""
    stu_dictionary.py

    It will generate the dictionary (tag_name, E)
    E is the set of every word calculated by TF-IDF
"""

import stu_misc
#from stu_tags import tags
from stu_questions import *
from sklearn.feature_extraction.text import TfidfVectorizer


def transform_text(documents):
    tfidf_model = TfidfVectorizer(min_df = 0.1, max_df = 0.6, stop_words='english')
    tfidf = tfidf_model.fit_transform(documents)
    return tfidf_model.get_feature_names()

def generate_string(wlist):
    return ' '.join([w for w in wlist])

# sample of tags
tags = ['c++','java','sql','python','scala','windows','linux','unix','c#','c']
print('Number of tags to process: ', len(tags))

with open(stu_misc.DICT_FILE, 'w+') as f:
    print('Generate the tags into ',DICT_FILE,'...')
    for t in tags:
        print('Questions from ', t)
        qs = getQuestionsFromTag(t)

        # I don't take tags with less than 10 questions that use it
        n = len(qs)
        if(n < 100):
            print('FAILURE - ',t, ' ignored: not enough questions: ', n)
            continue
        else:
            print('SUCCESS - ', t, ' has ', len(qs), ' questions')
            fwords = transform_text(getDocuments(qs))
            print('Number of words: ', len(fwords))
            # put it in a file
            f.write(t)
            f.write(',')
            f.write(generate_string(fwords))
            f.write('\n')
    print('Generated every tags ...')

"""
print('Questions from c++')
qs = getQuestionsFromTag('c++')
print('number of questions')
print(len(qs))
#print('check')
#print(all(q >= stu_misc.MIN_ID and q <= stu_misc.MAX_ID and (q % 10) == 0 for q in qs))
print('get documents')
qdoc = getDocuments(qs)
print(len(qdoc))
fwords = transform_text(qdoc)
print('number of world: ', len(fwords))
print(fwords)
"""
