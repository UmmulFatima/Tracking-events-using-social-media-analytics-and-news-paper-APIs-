import re

import pandas as pd
from tabulate import tabulate
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
# df = pd.read_csv('tweetsManual.csv', sep=';')
# print(tabulate(df, headers='keys', tablefmt='psql'))

data = pd.read_csv('ManualLabelledTweets.csv', sep=';')
Keywords = data['keywords'].tolist()
# print('repeated keywords:', set([x for x in Keywords if Keywords.count(x) > 1]))

stopword_set = set(stopwords.words('english'))
t = []
tweets = data['text']
for i in tweets:
    i = i.split()
    i = i.apply((lambda x: [item for item in x if item not in stopword_set]))
    # keep only words
    regex_pat = re.compile(r'[^a-zA-Z\s]', flags=re.IGNORECASE)
    i = i.str.replace(regex_pat, '')

    # join the cleaned words in a list
    i.str.join("")
    t.append(i)

# The list of lists
flattened_list = []

# flatten the lis
for x in t:
    for y in x:
        flattened_list.append(y)
print(flattened_list)

# count frequency of a term in Keywords list
counts = Counter(flattened_list)
print(counts)
# print most common repeated words and sorted them
print(counts.most_common(4))
print(tabulate(counts.most_common(4), headers=['keyword', 'frequency'], tablefmt='orgtbl'))

counts_most_common = dict(Counter(Keywords).most_common(4))
labels, values = zip(*counts_most_common.items())

# sort values in descending order
indSort = np.argsort(values)[::-1]

# rearrange data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.35

plt.bar(indexes, values)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.xlabel('keywords')
plt.ylabel('frequency')
#plt.show()