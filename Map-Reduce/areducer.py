#!/usr/bin/env python

import sys
import operator

topvideo = {}

for line in sys.stdin: 
    line = line.strip()
    inputs = line.split(',')
    vid = ",".join(inputs[:-1])
    sale = inputs[-1]
    try: 
        sale = float(sale)
        topvideo[vid] = sale
    except: 
        continue

sort = sorted(topvideo, key=topvideo.get, reverse=True)

n = 0 
for v in sort:
    if n < 10: 
        print '%s,%s' % (v, topvideo[v])
        n = n + 1
    else: 
     break
