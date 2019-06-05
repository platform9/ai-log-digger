import sys
import os
import io

from processor import process_line
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
    examples = [line]
    example_counts = vectorizer.transform(examples)
    prediction_proba = classifier.predict_proba(example_counts)
    return prediction_proba

#predict(process_line(sys.argv[1]))