#!/usr/bin/env python

import sys


for line in sys.stdin:
  line = line.strip()
  attributes= line.split(',')
  index = 0 
  for a in attributes:
    try:  
      if len(a) == 4 and a.isdigit():
        genre = attributes[index + 1] # index is 'year', index + 1 is Genre
        sale = attributes[index + 7] # index(year) + 7 = global_Sales
        print '%s,%s' % (genre, sale)
        break
      else: 
        index += 1
    except: 
      index += 1
