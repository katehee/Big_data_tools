#!/usr/bin/env python

import sys

for line in sys.stdin:
  line = line.strip()
  attributes= line.split(',')
  index = 0 
  for a in attributes:
    try:  
      if len(a) == 4 and a.isdigit():
        year = a
        sale = attributes[index + 3]
        print '%s,%s' % (year, sale)
        break
      else: 
        index += 1
    except: 
      index += 1