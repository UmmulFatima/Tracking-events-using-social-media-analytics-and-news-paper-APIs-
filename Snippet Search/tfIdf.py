from __future__ import unicode_literals

import sys
from itertools import product
from collections import Iterable

from nltk import WordNetLemmatizer
from nltk.corpus import stopwords,wordnet
import re, csv
from string import punctuation
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet as wn


with open('twitter_en.txt', 'r') as f:
    stopwords_list = []
    for line in f:
        stopwords_list.append(line)
    stopwords_list[:] = [line.rstrip('\n') for line in stopwords_list]

stopwords = set(stopwords.words('english'))
pun = list(punctuation)


# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).

def stripNonAlphaNum(text):
    texts = re.compile(r'\W+', re.UNICODE).split(text)
    return texts


# Given a list of words, remove any that are
# in a list of stop words and punctuation

def removeStopwords(wordlist, stopwords):
    text = [w for w in wordlist if w not in stopwords]
    text = [w for w in text if not w.isnumeric()]
    return text


def remove_punctuaions(wordlist, pun):
    text = [w for w in wordlist if w not in pun]
    return text


# Given a list of words, return a dictionary of word-frequency pairs.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

document_text = open('snippet_google.txt', 'r')
text_string = document_text.read().lower()

fullwordlist = stripNonAlphaNum(text_string)
word_list = removeStopwords(fullwordlist, stopwords)
word_list = [w for w in word_list if w not in stopwords_list]
word_list = remove_punctuaions(word_list, pun)
dictionary = wordListToFreqDict(word_list)
sortdict = sortFreqDict(dictionary)

top3_terms = sortdict[:3]
tfIdf_event = []
tfIdf_frequency = []
for s in sortdict[:9]:
    tfIdf_event.append(s[1])
    tfIdf_frequency.append(s[0])
# print(tfIdf_event, tfIdf_frequency)





###############3test########################
# doc_complete = ['Tweet with a location. You can add location information to your Tweets, such as your city or precise location, from the web and via third-party applications.',
#                 'The latest Tweets from Debate Presidencial (@Debate2012RD). Iniciativa ciudadana por el #DebatePresidencial 2012 en República Dominicana. #Debate2012. República',
#                 'The latest Tweets from Oman Debate 2012 (@OmanDebate2012). Oman Economic Review in association with Capital Market Authority (CMA) is holding the 4th annual Oman']
#
# lemma = WordNetLemmatizer()
# wordlist = []
# for doc in doc_complete:
#     doc = doc.replace("#", "").replace("_", " ")  # Removing HASH symbol
#     doc = re.sub(r'[^\x00-\x7f]', r'', doc)  # Removing the Hex characters(emoji)
#     stop_free = " ".join([i for i in doc.lower().split() if i not in stopwords])
#     stop_free = " ".join([i for i in stop_free.lower().split() if i not in stopwords_list])
#     # removing punctuations
#     text = re.sub(r'[^a-zA-Z0-9@\S]', ' ', stop_free)
#     remove_pun = str.maketrans({key: None for key in punctuation})
#     punc_free = text.translate(remove_pun)
#     f = punc_free.split()
#     wordlist.append(f)
# print('norm', wordlist)
#
# fullwordlist=[]
# for item in wordlist:
#     if isinstance(item, (str, int, bool)):
#         fullwordlist.append(item)
#     elif isinstance(item, dict):
#         for i in item.items():
#             fullwordlist.extend(i)
#     else:
#         fullwordlist.extend(list(item))
# print(fullwordlist)
# dictionary = wordListToFreqDict(fullwordlist)
# sortdict = sortFreqDict(dictionary)
# print(sortdict)
#######################3test###########################






#######################################

# string matching between tf-idf(three highest terms) event and
# manually labelled event topic descriptions from Event2012 database
# newEventlist = labelled events from Events2012 database

# events_2012 = []
# with open("event_descriptions.tsv") as tsvfile:
#     tsvreader = csv.reader(tsvfile, delimiter="\t")
#     for line in tsvreader:
#         event = line[1]
#         events_2012.append(event)
#
# newEventlist = list()
# for item in range(len(events_2012)):
#     event = events_2012[item]
#
#     # removing punctuations
#     event = re.sub(r'[^a-zA-Z0-9@\S]', ' ', event)
#     remove_pun = str.maketrans({key: None for key in punctuation})
#     event = event.translate(remove_pun)
#
#     # removing hexa-character
#     event = re.sub(r'[^\x00-\x7f]', r'', event)
#
#     # split the element string into a list of words
#     itemWords = event.split()
#
#     # removing stopwords from twitter stopwordlist and nltk stopword
#     itemWords = [w for w in itemWords if w not in stopwords_list]
#     itemWords = [w for w in itemWords if w not in stopwords]
#
#     if bool(set(tfIdf_event) & set(itemWords)):
#             matching = (set(tfIdf_event) & set(itemWords))
#             matching_word = len(set(tfIdf_event) & set(itemWords))
#             print('the number of matching word betweet event2012 database and tfidf event', matching_word, matching)
#
#             if matching:
#                 # semantic similarity between tfIdf_event and event2012
#                 # wu-palmer semantic similarity and itemwords = list of Event words
#                 count = 0
#                 temp_sum = 0.0
#
#                 for w1 in range(len(tfIdf_event)):
#                     sim_list = []
#                     for w2 in range(len(itemWords)):
#                         t1 = tfIdf_event[w1]
#                         d1 = itemWords[w2]
#                         allsyn1 = set(ss for ss in wordnet.synsets(t1))
#                         allsyn2 = set(ss for ss in wordnet.synsets(d1))
#                         syn_sim = []
#                         for s1 in allsyn1:
#                             for s2 in allsyn2:
#                                 if wordnet.wup_similarity(s1, s2) is not None:
#                                     wup_sim = wordnet.wup_similarity(s1, s2)
#                                 else:
#                                     wup_sim = 0.0
#                                 syn_sim.append(wup_sim)
#
#                         # maximum similaity of allsyn1 and allsyn2 for t1, d1
#                         if len(syn_sim) == 0:
#                             best_synset_similarity = 0.0
#                         else:
#                             best_synset_similarity = max(syn_sim)
#                         sim_list.append(best_synset_similarity)
#                     temp_sim_score = max(sim_list)
#                     temp_sum = temp_sum + temp_sim_score
#                     count += 1
#                 if count == 0:
#                     print('error')
#                 else:
#                     print('tf-Idf wu-palmer semantic similarity', temp_sum/count)