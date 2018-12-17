import csv
from difflib import SequenceMatcher
from nltk.corpus import stopwords
import texttable as tt

with open('../stopwords/twitter_en.txt', 'r') as f:
    stopwords_list = []
    for line in f:
        stopwords_list.append(line)
    stopwords_list[:] = [line.rstrip('\n') for line in stopwords_list]
stopwords = set(stopwords.words('english'))

annotated_events_2012 = []
with open("../data/event_descriptions.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        event = line[1]
        annotated_events_2012.append(event)


mabbed_generated_topic_list =[]
with open("../output/detectedEvent_mainTerm.txt", 'r') as txtfile:
    for line in txtfile:
        line = line.replace("'", "")
        line = line.replace(",", '')
        mabbed_generated_topic_list.append(line)
    mabbed_generated_topic_list[:] = [line.rstrip('\n') for line in mabbed_generated_topic_list]

dict = dict()
i = 0
ss = []
count = []
number_of_match = []
for term in mabbed_generated_topic_list:
    a = []
    string_matching_ratio = []
    for event in annotated_events_2012:
        generated_event = term.replace('[', ' ')
        generated_event = generated_event.replace(']', ' ')

        ratio = SequenceMatcher(None, generated_event, event).ratio()
        if ratio is not None:
            string_matching_ratio.append(ratio)
        generated_event = set(generated_event.split())
        annotated_event = set(event.split())

        if generated_event.intersection(annotated_event):
            matching = (generated_event.intersection(annotated_event))
            matching_score = len(matching)
            a.append(matching_score)
            #if matching_score >= 2:
               # print(matching)
    s = max(string_matching_ratio)
    ss.append(s)
    i = i + 1
    count.append(i)
    # dict[i] = len(a)
    number_of_match.append(len(a))
    # print('event', i, len(a))

tab = tt.Texttable()
headings = ['Serial','Generated events','Matching ratio', 'Number of match']
tab.header(headings)

for row in zip(count, mabbed_generated_topic_list, ss, number_of_match):
    tab.add_row(row)

s = tab.draw()
print(s)