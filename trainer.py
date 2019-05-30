# Sample command: python train.py success_samples/ failure_samples/ 'Node xyx disconnected'
import sys
import os
import io

from pandas import DataFrame
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


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
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

examples = ['Master d3538f42-6b9d-4650-9f4f-f80f518b6a38 disconnected.', 'Node added', 'Node d91f5623-3521-4ac9-8dfd-b6dbba07c7aa became worker']
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)

print predictions

if len(sys.argv) > 3:
    to_predict = sys.argv[3]
    example_counts = vectorizer.transform([to_predict])
    predictions = classifier.predict(example_counts)
    print predictions





