# -*- coding: utf-8 -*-
'''
Created on Dec 29, 2015
@author: hanhanwu
using F1 score to evaluate the results of NLP
F1 = 2*(precision*recall)/(precision+recall)
precision = TP/(TP+FP)
recall = TP/(TP+FN)
'''
import nltk

def main():
    txt = 'Mr. Green killed Colonel Mustard in the study with the candlestick.'
    ground_truth = ['Mr. Green', 'killed', 'Colonel Mustard', 'study', 'candlestick']  # real abstract
    
    tokens = [w for w in nltk.tokenize.word_tokenize(txt)]
    fdist = nltk.FreqDist(tokens).keys()[:7]  # machine generated abstract
    
    TP = 0.0
    FP = 0.0
    FN = 0.0
    for w in fdist:
        if w in ground_truth:
            TP += 1.0
        else:
            FP += 1.0
    for w in ground_truth:
        if w not in fdist:
            FN += 1.0
            
    my_precision = TP/(TP + FP)
    my_recall = TP/(TP + FN)
    F1 = 2*(my_precision*my_recall)/(my_precision+my_recall)
    print F1
            
    
if __name__ == '__main__':
    main()
