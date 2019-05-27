import sys
import analyzer

analyzer.analyze("This is bad.")

hotel_rev = ["Great place to be when you are in Bangalore.",
"The place was being renovated when I visited so the seating was limited.",
"Loved the ambience, loved the food",
"The food is delicious but not over the top.",
"Service - Little slow, probably because too many people.",
"The place is not easy to locate",
"Mushroom fried rice was tasty"]

for sentence in hotel_rev:
     print sentence
     s = analyzer.analyze(sentence)
     print 'Sentiment: ' + str(s)
