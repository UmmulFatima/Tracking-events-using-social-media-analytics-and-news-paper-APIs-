import sys
from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# get path to script's directory
currdir = path.dirname(__file__)


def create_wordcloud(text):
    # create numpy araay for wordcloud mask image
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))

    # create set of stopwords
    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white",
                   max_words=200,
                   mask=mask,
                   stopwords=stopwords)

    # generate wordcloud
    wc.generate(text)

    # save wordcloud
    wc.to_file(path.join(currdir, "wc.png"))


if __name__ == "__main__":
    file = open("snippet_google.txt", "r")
    documents = file.read()

    # generate wordcloud
    create_wordcloud(documents)
