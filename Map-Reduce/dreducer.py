#!/usr/bin/env python

import sys
import operator

topgenre = {}

for line in sys.stdin: 
    line = line.strip()
    inputs = line.split('\t')
    name = inputs[0]
    genre = inputs[1]
    sale = inputs[2]
    try: 
        sale = float(sale)
        topgenre[genre] = sale
    except: 
        continue

sort = sorted(topgenre, key=topgenre.get, reverse=True)

n = 0 
for g in sort:
    if n < 10: 
        print '%s,%s' % (g, topgenre[g])
        n = n + 1
    else: 
     break
