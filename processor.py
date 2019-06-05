import sys
import nltk
import re

def has_numbers(inputString):
     return bool(re.search(r'\d', inputString))

def process_line(line):
    line = " ".join(w for w in nltk.wordpunct_tokenize(line) \
           if not has_numbers(w) and w.isalnum()) 
    return line

#print process_line(sys.argv[1])

