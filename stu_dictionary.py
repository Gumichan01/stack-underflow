
"""
    stu_dictionary.py

    It will generate the dictionary (tag_name, E)
    E is the set of every word calculated by TF-IDF
"""

import stu_misc
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
        Convert list of element to a string that contains every elements
    """
    return ' '.join([w for w in wlist])

v = 0
min_t = 48
with open(stu_misc.DICT_FILE, 'w+') as f:
    print('Generate the tags into ',stu_misc.DICT_FILE,'...')
    for lt in lookup_table:

        # process the tag
        print('Questions from ', lt)
        qs = get_documents(lookup_table[lt])

        # I don't take tags with less than 10 questions that use it
        n = len(qs)
        if(n < min_t):
            print('FAILURE - ',lt,' ignored: not enough questions: ', n)
            continue
        else:
            print('SUCCESS - ',lt,' has ',n,' questions')
            fwords = transform_text(qs)
            print('Number of words: ', len(fwords))
            # put it in a file
            f.write(lt)
            f.write(',')
            f.write(generate_string_from(fwords))
            f.write('\n')
            v += 1
            print('Tags that has been read: ', v)
    print('Generated every tags ...')
