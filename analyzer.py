import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def get_sentiment(str):
    si = sia.polarity_scores(str)
    # print si
    return si['compound']

def analyze(str):
    return get_sentiment(str)
#print 'Text: ' + sys.argv[1]
#print 'Sentiment: ' + str(analyze(sys.argv[1]))
