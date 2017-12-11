
"""
    stu_dictionary.py

    It will generate the dictionary (tag_name, E)
    E is the set of every word calculated by TF-IDF
"""

#from stu_tags import tags
from stu_questions import *
from sklearn.feature_extraction.text import TfidfVectorizer

def transform_text(documents):
    tfidf_model = TfidfVectorizer(min_df = 0.2, max_df = 0.7, stop_words='english')
    tfidf = tfidf_model.fit_transform(documents)
    return tfidf_model.get_feature_names()

"""
for t in tags:
    print('Questions from ', t.name)
    qs = getQuestionsFromTag('c++')

    # I don't take tags with less than 10 questions that use it
    if(len(qs) < 10):
        print(t.name, ' ignored: not enough questions')
        continue
    else:
        print(t.name, ' has ', len(qs), ' questions')
        fwords = transform_text(getDocuments(qs))
        print('number of world: ', len(fwords))
        print(fwords)
        # put it in a file
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
