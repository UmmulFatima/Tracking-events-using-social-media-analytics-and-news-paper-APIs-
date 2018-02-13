import numpy as np
import string
import math
import re
from nltk.corpus import stopwords
import nltk.corpus as corpus
from nltk.corpus import wordnet
import itertools as IT
from sematch.semantic.similarity import WordNetSimilarity
import  sys

wordnet = corpus.wordnet
sys.stdout = open('topicMatchingOutput.txt','wt')
class feval(object):
    """docstring for eval"""
    def mscore(self, list1, list2):
        a = np.array(list1)
        l1 = a.tolist()
        b = np.array(list2)
        l2 = b.tolist()
        list = []
        for w1 in l1:
            for w2 in l2:
                wordFromList1 = wordnet.synsets(w1)
                wordFromList2 = wordnet.synsets(w2)
                if wordFromList1 and wordFromList2:
                    s = wordFromList1[0].wup_similarity(wordFromList2[0])
                    if s == None:
                        s1 = 0.0
                    else:
                        s1 = s
                    list.append(s1)
                    print(w1, w2, s1)
        #print(max(list), list)
if __name__ == '__main__':

    devent = []
    tevent = []

    with open("event_details.txt", "r") as f1:
        for line in f1:
            term = line.replace('\n', '')
            terms = re.findall('[a-zA-Z]+', term)
            devent.append(terms)
    d = sum(devent, [])
    # print(d)

    with open("trending_event.txt", "r") as f2:
        for line in f2:
            term = line
            trend = term.replace('#', '')
            trends = trend.replace('\n', '')
            tevent.append(trends)
    # print(tevent)
    # for i in d:
    # 	for j in tevent:
    # 		#print(i,j)
    # 		if i == j:
    # 			print(i)
    # 		else:
    # 			print("nothing")

    ss = feval()
    ss.mscore(d, tevent)