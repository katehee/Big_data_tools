#!/usr/bin/env python

import sys
import operator

topsaleyear = {}

for line in sys.stdin: 
    line = line.strip()
    vid, sale = line.split(",")
    try: 
        sale = float(sale)
        topsaleyear[vid] = sale
    except: 
        continue

sort = sorted(topsaleyear, key=topsaleyear.get, reverse=True)

n = 0 
for v in sort:
    if n < 10: 
        print '%s,%s' % (v, topsaleyear[v])
        n = n + 1
    else: 
     break
