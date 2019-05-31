import sys
import os
import io

from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import cPickle

classifier = None
vectorizer = None

def predict(line):
    global classifier
    global vectorizer
    if not classifier:
        classifier = cPickle.load(open('model.sav', 'rb'))
        counts = cPickle.load(open('voc.sav', 'rb'))
        vectorizer = CountVectorizer(vocabulary=counts)
        #vectorizer = CountVectorizer()
        #vectorizer._validate_vocabulary()
    #examples = [line]
    #examples = ['Master d3538f42-6b9d-4650-9f4f-f80f518b6a38 disconnected.', 'Node d91f5623-3521-4ac9-8dfd-b6dbba07c7aa became worker']
    examples = [line]
    example_counts = vectorizer.transform(examples)
    prediction_proba = classifier.predict_proba(example_counts)
    predictions = classifier.predict(example_counts)
    #print line.replace('\n', '') + '\t' + str(prediction_proba)
    return prediction_proba

predict(sys.argv[1])