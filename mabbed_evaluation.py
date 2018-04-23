import re


class similarity(object):
    """docstring for similarity"""

    # def intersection(self, list1, list2):
    # return set(list1).intersection(list2)

    def sim(self, tevent, devent):
        cardinality_list = []
        for i in range(len(tevent)):
            common_event_name = set(devent).intersection(tevent[i])
            cardinality_of_intersection = len(common_event_name)
            cardinality_list.append(cardinality_of_intersection)
        min_similarity = min(cardinality_list)
        max_similarity = max(cardinality_list)
        Similarity = (min_similarity / max_similarity)
        return Similarity


if __name__ == '__main__':

    detectedEvent = []
    trendEvent = []

    with open("output/detectedEvent.txt", "r") as f1:
        for line in f1:
            term = line.replace('\n', '')
            terms = re.findall('[a-zA-Z]+', term)
            detectedEvent.append(terms)
    DetectedEvent = sum(detectedEvent, [])
    # print(DetectedEvent)

    with open("trends/twitter_trends.txt", "r") as f2:
        for line in f2:
            term = line
            trend = term.replace('#', '')
            trends = trend.replace('\n', '')
            trendEvent.append(trends)
    # print(trendEvent)

    # finding common word between detected event and twitter trend event
    # d = {}
    # for word in DetectedEvent:
    #     d[word] = True
    # for word in trendEvent:
    #     if d[word]:
    #         print(word)

    common_event = set(trendEvent).intersection(DetectedEvent)
    print(common_event)

    similarity_score = similarity()
    s = similarity_score.sim(trendEvent, DetectedEvent)
    print(s)
