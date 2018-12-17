import csv
import re
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.corpus import stopwords, wordnet


with open('twitter_en.txt', 'r') as f:
    stopwords_list = []
    for line in f:
        stopwords_list.append(line)
    stopwords_list[:] = [line.rstrip('\n') for line in stopwords_list]
stopwords = set(stopwords.words('english'))
pun = list(punctuation)


def display_topics(H, W, feature_names, documents, no_top_words, no_top_documents):
    for topic_idx, topic in enumerate(H):
        # print("Topic %d:" % (topic_idx))
        topic = " ".join([feature_names[i]
                          for i in topic.argsort()[:-no_top_words - 1:-1]])
        print("Topic %d:" % (topic_idx), topic)
        # top_doc_indices = np.argsort( W[:,topic_idx] )[::-1][0:no_top_documents]
        # for doc_index in top_doc_indices:
        # print('documents', documents[doc_index])


with open('snippet_google.txt') as f:
    documents = []

    for line in f:
        # Removing HASH symbol
        text = line.replace("#", "").replace("_", " ")
        # print('removing hash character and underscore', tweet_text)

        # Removing the Hex characters(emoji)
        text = re.sub(r'[^\x00-\x7f]', r'', text)
        # print('Removing the Hex characters', tweetText)

        # removing punctuations
        text = re.sub(r'[^a-zA-Z0-9@\S]', ' ', text)
        remove_pun = str.maketrans({key: None for key in punctuation})
        text = text.translate(remove_pun)
        documents.append(text)

    # Remove new line characters
    documents = [re.sub('\s+', ' ', sent) for sent in documents]

    # Remove distracting single quotes
    documents = [re.sub("\'", "", sent) for sent in documents]

no_features = 1000

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=3, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()

# Run LDA
lda_model = LatentDirichletAllocation(n_topics=3, max_iter=5, learning_method='online', learning_offset=50.,
                                      random_state=0).fit(tf)

lda_W = lda_model.transform(tf)
lda_H = lda_model.components_

no_top_words = 4
no_top_documents = 3
display_topics(lda_H, lda_W, tf_feature_names, documents, no_top_words, no_top_documents)


###############################################

# computing common words between LDA_topics and Event2012 topic
# LDA top 3 topics
LDA_topics = []
with open('output.txt') as file:
    for line in file:
        LDA_topics.append(line)
lda_topics = [re.sub('\s+', ' ', sent) for sent in LDA_topics]
print('lda topics', lda_topics)

# Event description from Event2012
events_2012 = []
with open("event_descriptions.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        event = line[1]
        events_2012.append(event)
    print('event 2012 list', events_2012)

for event in events_2012:
    # removing punctuations
    event = re.sub(r'[^a-zA-Z0-9@\S]', ' ', event)
    remove_pun = str.maketrans({key: None for key in punctuation})
    event = event.translate(remove_pun)

    # removing hexa-character
    event = re.sub(r'[^\x00-\x7f]', r'', event)

    # split the element string into a list of words
    EventWords = event.split()

    # removing stopwords from twitter stopwordlist and nltk stopword
    Event2012_Words = [w for w in EventWords if w not in stopwords_list]
    Event2012_Words = [w for w in Event2012_Words if w not in stopwords]

    string_matching = []
    count = 0
    tempsum = 0.0
    for topic in lda_topics:
        lda_Topic = topic.lower().split()
        intersection = set(lda_Topic) & set(Event2012_Words)
        number_of_common_words = len(intersection)
        string_matching.append(number_of_common_words)
        sim_list = []
        for w1 in lda_Topic:
            for d1 in EventWords:
                allsyn1 = set(ss for ss in wordnet.synsets(w1))
                allsyn2 = set(ss for ss in wordnet.synsets(d1))
                syn_sim = []
                for s1 in allsyn1:
                    for s2 in allsyn2:
                        if wordnet.wup_similarity(s1, s2) is not None:
                            wup_sim = wordnet.wup_similarity(s1, s2)
                        else:
                            wup_sim = 0.0
                        syn_sim.append(wup_sim)

                # maximum similaity of allsyn1 and allsyn2 for t1, d1
                if len(syn_sim) == 0:
                    best_synset_similarity = 0.0
                else:
                    best_synset_similarity = max(syn_sim)
                sim_list.append(best_synset_similarity)
        # print(sim_list)
        # print('max of t1 and d', max(sim_list))
        count += 1
        tempsum = tempsum + max(sim_list)
        # print(count, tempsum)
    if count == 0:
        print('exceptions')
    else:
        print('LDA_topic semantic similarity', tempsum / count)
    print('number of matching between LDA topic and EVENT (Event2012)', max(string_matching))
