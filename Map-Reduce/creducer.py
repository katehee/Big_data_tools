#!/usr/bin/env python

import sys

current_year = None
current_sale = 0
year = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    year, sale = line.split(',')

    try:
        sale = float(sale)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue


    if current_year == year:
        current_sale += sale
    else:
        if current_year:
            print '%s,%s' % (current_year, current_sale)
        current_sale = sale
        current_year = year

if current_year == year:
    print '%s,%s' % (current_year, current_sale)