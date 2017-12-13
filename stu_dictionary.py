
"""
    stu_dictionary.py

    It will generate the dictionary (tag_name, E)
    E is the set of every word calculated by TF-IDF
"""

import stu_misc
from stu_tags import tags
from stu_questions import *
from sklearn.feature_extraction.text import TfidfVectorizer


def transform_text(documents):
    """
        Calculate the TF-IDF of the documents

        Arg:
            a list of documents
        Return:
            the feature names from the documents
    """
    tfidf_model = TfidfVectorizer(min_df = 0.1, max_df = 0.6, stop_words='english')
    tfidf = tfidf_model.fit_transform(documents)
    return tfidf_model.get_feature_names()

def generate_string_from(wlist):
    """
        Convert list of element to a string that conains every elements
    """
    return ' '.join([w for w in wlist])

# sample of tags (for testing)
#tags = ['c++','java','sql','python','scala','windows','linux','unix','c#','c']
max_t = 100
print('Number of tags to process: ', len(tags))
print('Maximum number of tags to process: ', max_t)


v = 0
max_v = 4
with open('stu_misc.DICT_FILE, 'w+') as f:
    print('Generate the tags into ',stu_misc.DICT_FILE,'...')
    for t in tags:
        if v == max_v :
            break

        # process the tag
        print('Questions from ', t)
        qs = get_question_from(t)

        # I don't take tags with less than 10 questions that use it
        n = len(qs)
        if(n < max_t):
            print('FAILURE - ',t, ' ignored: not enough questions: ', n)
            continue
        else:
            print('SUCCESS - ', t, ' has ', len(qs), ' questions')
            fwords = transform_text(get_documents(qs))
            print('Number of words: ', len(fwords))
            # put it in a file
            f.write(t)
            f.write(',')
            f.write(generate_string_from(fwords))
            f.write('\n')
            v += 1
            print('Tags that has been read: ', v)
    print('Generated every tags ...')

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
fwords = transform_text(qdoc)
print('number of world: ', len(fwords))
print(fwords)
"""
