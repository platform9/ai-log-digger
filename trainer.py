# Sample command: python train.py success_samples/ failure_samples/ 'Node xyx disconnected'
import sys
import os
import io

from processor import process_line
from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import cPickle


def readFiles(path):
    for root, clusnames, filenames in os.walk(path):
        for clusname in clusnames:
            path = os.path.join(root, clusname)
            for clusroot, dirnames, logfiles in os.walk(path):
                for logfile in logfiles:
                    logpath = os.path.join(path, logfile)
                    print 'Learning log file: ' + logpath
                    lines = []
                    f = io.open(logpath, 'r', encoding='latin1')
                    for line in f:
                        lines.append(process_line(line))
                    f.close()
                    message = ''.join(lines)
                    yield logpath, message

def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

success_samples = sys.argv[1]
failure_samples = sys.argv[2]

data = DataFrame({'message': [], 'class': []})
data = data.append(dataFrameFromDirectory(success_samples, 'success'))
data = data.append(dataFrameFromDirectory(failure_samples, 'failure'))

print data

vectorizer = CountVectorizer()
voc = vectorizer.fit(data['message'].values)
cPickle.dump(voc.vocabulary_, open('voc.sav', 'wb'))
counts = vectorizer.transform(data['message'].values)
feature_names = vectorizer.get_feature_names()
print 'Total feature names: ' + str(len(feature_names))

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)
cPickle.dump(classifier, open('model.sav', 'wb'))

if len(sys.argv) > 3:
    to_predict = sys.argv[3]
    example_counts = vectorizer.transform([to_predict])
    predictions = classifier.predict(example_counts)
    print predictions