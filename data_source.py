import sys
from predictor import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_prob_line(p):
    fmargin = (p[0][0] - p[0][1]) * 10
    scount = 0
    fcount = 0
    if fmargin < 0:
        scount = -int(fmargin)
    else:
        fcount = int(fmargin)
    return '{:<10}'.format('%.2f' % (p[0][0] *100) + '%') + \
           bcolors.OKGREEN + '{:>20}'.format('S'*scount) + \
           bcolors.ENDC + '|' + \
           bcolors.WARNING + '{:<20}'.format('F'*fcount) + \
           bcolors.ENDC

with open(sys.argv[1], "r") as d:
    print '{:<60}'.format('Line') + '{:<10}'.format('Failure Prob')
    error_logs = []
    for line in d:
        p = predict(line)
        print '{:<60}'.format(line.replace('\n', '')) + get_prob_line(p)
        if p[0][0] > 0.8:
            error_logs.append(line)

print 'Suspicious logs:'
for line in error_logs:
    print line

