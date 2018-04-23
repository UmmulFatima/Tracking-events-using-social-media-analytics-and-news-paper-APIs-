import re


class similarity(object):
    """docstring for similarity"""

<<<<<<< HEAD
    # def intersection(self, list1, list2):
    # return set(list1).intersection(list2)

    def sim(self, tevent, devent):
        cardinality_list = []
        for i in range(len(tevent)):
            common_event_name = set(devent).intersection(tevent[i])
            cardinality_of_intersection = len(common_event_name)
            cardinality_list.append(cardinality_of_intersection)
=======
    #def intersection(self, list1, list2):
        #return set(list1).intersection(list2)

    def sim(self, tevent, devent):
        cardinality_list = []
        for i in devent:
            element = devent[i]
            common_term = set(element).intersection(tevent)
            cardinality_of_intersection = len(common_term)
            print(element, common_term, cardinality_of_intersection)
            cardinality_list.append(cardinality_of_intersection)
        print(cardinality_list)
>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
        min_similarity = min(cardinality_list)
        max_similarity = max(cardinality_list)
        Similarity = (min_similarity / max_similarity)
        return Similarity


if __name__ == '__main__':
<<<<<<< HEAD

    detectedEvent = []
    trendEvent = []

    with open("output/detectedEvent.txt", "r") as f1:
=======
    detectedEvent = []
    trendEvent = []

    with open("detectedEvent.txt", "r") as f1:
>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
        for line in f1:
            term = line.replace('\n', '')
            terms = re.findall('[a-zA-Z]+', term)
            detectedEvent.append(terms)
    DetectedEvent = sum(detectedEvent, [])
<<<<<<< HEAD
    # print(DetectedEvent)

    with open("trends/twitter_trends.txt", "r") as f2:
=======
    print(DetectedEvent)

    with open("twitter_trend.txt", "r") as f2:
>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
        for line in f2:
            term = line
            trend = term.replace('#', '')
            trends = trend.replace('\n', '')
            trendEvent.append(trends)
<<<<<<< HEAD
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
=======
    print(trendEvent)

    sim = similarity()
    sim.sim(DetectedEvent, trendEvent)
    print(sim)
>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
