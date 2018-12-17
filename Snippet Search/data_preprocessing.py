from nltk.corpus import stopwords
import re
import itertools
import gensim
from gensim.utils import simple_preprocess
import logging
import warnings

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)
warnings.filterwarnings("ignore", category=DeprecationWarning)

stop_words = stopwords.words('english')
# stop_words.extend(['from', 'subject', 're', 'edu', 'use'])


# Let’s tokenize each sentence into a list of words, removing punctuations and unnecessary characters altogether

def sent_to_words(sentences):
    for sentence in sentences:
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

def removeStopwords(wordlist, stopwords):
    text = [w for w in wordlist if w not in stopwords]
    text = [w for w in text if not w.isnumeric()]
    return text

with open('snippet_google.txt') as f:
    f_list = []
    for line in f:
        f_list.append(line)
    # print('converted list of files', f_list)

    # Remove new line characters
    data = [re.sub('\s+', ' ', sent) for sent in f_list]
    # print('new line removed', data)

    # Remove distracting single quotes
    data = [re.sub("\'", "", sent) for sent in data]

    # removing punctuations and unnecessary characters
    data_words = list(sent_to_words(data))

    combined = list(itertools.chain.from_iterable(data_words))
    # create corpus
    print('corpus', combined)