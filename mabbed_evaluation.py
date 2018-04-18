import re


class similarity(object):
    """docstring for similarity"""

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
        min_similarity = min(cardinality_list)
        max_similarity = max(cardinality_list)
        Similarity = (min_similarity / max_similarity)
        return Similarity


if __name__ == '__main__':
    detectedEvent = []
    trendEvent = []

    with open("detectedEvent.txt", "r") as f1:
        for line in f1:
            term = line.replace('\n', '')
            terms = re.findall('[a-zA-Z]+', term)
            detectedEvent.append(terms)
    DetectedEvent = sum(detectedEvent, [])
    print(DetectedEvent)

    with open("twitter_trend.txt", "r") as f2:
        for line in f2:
            term = line
            trend = term.replace('#', '')
            trends = trend.replace('\n', '')
            trendEvent.append(trends)
    print(trendEvent)

    sim = similarity()
    sim.sim(DetectedEvent, trendEvent)
    print(sim)
