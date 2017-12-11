
"""
    stu_dictionary.py

    It will generate the dictionary (tag_name, E)
    E is the set of every word calculated by TF-IDF
"""

#from stu_tags import tags
from stu_questions import *
from sklearn.feature_extraction.text import TfidfVectorizer

def transform_text(documents):
    tfidf_model = TfidfVectorizer(min_df = 0.1, max_df = 0.5)
    tfidf = tfidf_model.fit_transform(documents)
    return tfidf


#print('Questions from c++')
qs = getQuestionsFromTag('c++')
print('number of questions')
print(len(qs))
print('check')
print(all(q >= stu_misc.MIN_ID and q <= stu_misc.MAX_ID and (q % 10) == 0 for q in qs))
print('get documents')
qdoc = getDocuments(qs)
print(len(qdoc))
print(transform_text(qdoc))
