import csv
import re
import pandas as pd
import numpy as np
from tabulate import tabulate


class similarity(object):
    """docstring for similarity"""

    def sim(self, tevent, devent):
        # step2: finding similarity between between detected event and twitter trend event
        # intersection = set(tevent).intersection(devent)
        # print(intersection)
        cardinality_list = []
        for i in range(len(tevent)):
            common_event_name = set(devent).intersection(tevent[i])
            cardinality_of_intersection = len(common_event_name)
            cardinality_list.append(cardinality_of_intersection)
        min_similarity = min(cardinality_list)
        max_similarity = max(cardinality_list)
        Similarity = (min_similarity / max_similarity)
        return Similarity

    def tf_detected_event(self, Detected_Event):
        # Data frame to show the detected event is exist in each tweet.
        # if a detected event term is in tweet then labeling that term as Event(1) otherwise not event(0)
        # finding term frequency of term as a event
        df = pd.read_csv('tweets/tweets20180423-195304.csv')
        tweets = df['text']
        matrix = np.zeros(shape=(len(Detected_Event), len(tweets)))
        # print(matrix.size, len(tweets), len(DetectedEvent))
        for i in range(len(Detected_Event)):
            for j in range(len(tweets)):
                tweet = tweets[j]
                Event = Detected_Event[i]
                if Event in tweet:
                    matrix[i][j] = 1.0
                else:
                    matrix[i][j] = 0.0
        df = pd.DataFrame(matrix)
        # print(df)
        # print(df.astype(bool).sum(axis=1))
        df = pd.DataFrame({'col_two': Detected_Event,
                           'column_3': df.astype(bool).sum(axis=1)})
        print(tabulate(df, headers='keys', tablefmt='psql'))

    def Manual_labelling(self):
        # Step3: finding intersection between between detected event and manual keywords
        # manual keywords = assigning a keywords for each tweet manually

        keywords = []
        with open("tweets/tweets_manual_labelling20180430-122818.csv", "r") as ff:
            csv_reader = csv.reader(ff, delimiter=';')
            header = next(csv_reader)
            text_column_index = header.index('keywords')
            for lined in csv_reader:
                keyword = lined[text_column_index]
                keywords.append(keyword)
        print(keywords)


if __name__ == '__main__':
    detectedEvent = []
    trendEvent = []
    with open("output/detectedEvent.txt", "r") as f1:
        for line in f1:
            term = line.replace('\n', '')
            terms = re.findall('[a-zA-Z]+', term)
            detectedEvent.append(terms)
    DetectedEvent = sum(detectedEvent, [])
    with open("trends/twitter_trends.txt", "r") as f2:
        for line in f2:
            term = line
            trend = term.replace('#', '')
            trends = trend.replace('\n', '')
            trendEvent.append(trends)

    similarity_score = similarity()
    similarity_score.tf_detected_event(DetectedEvent)
    similarity_score.sim(trendEvent, DetectedEvent)
    similarity_score.Manual_labelling()
