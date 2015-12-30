'''
Created on Dec 21, 2015
@author: hanhanwu
nltk built-in collocation cannot return the data structure to let you manipulate the results
This module tells how to create a built-in collocation
'''
import nltk
from nltk.metrics import BigramAssocMeasures
import json

def main():
    f_path = '[change to your googleplus_posts.json location]'
    data = json.loads(open(f_path).read())
    
    all_tokens = [token for activity in data for token in activity['object']['content'].lower().split()]
    
    # The number of collocations you want to get
    N = 25
    finder = nltk.BigramCollocationFinder.from_words(all_tokens)
    finder.apply_freq_filter(2)
    finder.apply_word_filter(lambda w: w in nltk.corpus.stopwords.words('english'))
    scorer = BigramAssocMeasures.jaccard
    collocations = finder.nbest(scorer, N)
    
    for collocation in collocations:
        c = ' '.join(collocation)
        print c
    
if __name__ == '__main__':
    main()

