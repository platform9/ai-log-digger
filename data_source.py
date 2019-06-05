import sys
import json
from predictor import *
from processor import process_line

with open(sys.argv[1], "r") as d:
    print 'Processing ' + sys.argv[1]
    error_logs = {}
    i = 1
    for l in d:
        pl = process_line(l)
        p = predict(pl)
        if p[0][0] > 0.995: # Threshold 99.5 % 
            if pl in error_logs.keys():
                error_logs[pl]['count'] += 1
            else:
                error_logs[pl] = {'line': i,
                                  'text': l,
                                  'count': 1}
        i += 1

if len(error_logs) > 0:
    print '\nThis looks like a failure scenario.\n'
    i = 1
    for pl in error_logs.keys():
        print 'Evidence %d:' % (i)
        print json.dumps(error_logs[pl], indent=4)
        i += 1