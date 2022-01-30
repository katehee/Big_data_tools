#!/usr/bin/env python
import sys

for line in sys.stdin:
  line = line.strip()
  attributes= line.split(',')
  index = 0 
  for a in attributes:
    try:  
      if len(a) == 4 and a.isdigit():
        name = ",".join(attributes[:index - 1])
        # index is 'year', index - 1 is platform, index [:platform index] is video game name
        sale = attributes[index + 3] # index(year) + 3 = NA_Sales
        print '%s,%s' % (name, sale)
        break
      else: 
        index += 1
    except: 
      index += 1
