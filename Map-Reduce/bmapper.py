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
        genre = attributes[index + 1] # index is 'year', index + 1 is Genre
        gsale = attributes[index + 7] # index(year) + 7 = global_Sales
        print '%s\t%s\t%s' % (name, genre, gsale)
        break
      else: 
        index += 1
    except: 
      index += 1
