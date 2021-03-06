#!/usr/bin/env python

import sys
import operator

topnwords = {}  #dictionary to sort the words

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if len(words) == 2:
        try:
            count = int(words[1])   # word count
            topnwords[words[0]] = count # add word and count to dictonary
        except:
            continue

# list of words sorted by count
sort = sorted(topnwords, key=topnwords.get, reverse=True)

n = 0   #counter to only print upto top 10 words
for w in sort:    #iterate through all words sorted by count
    if n < 10:      # print up to top 10 words
        print '%s\t%s' % (w, topnwords[w])
        n = n + 1
    else:
        continue