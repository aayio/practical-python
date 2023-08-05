# Bonus: How would you modify this example to additionally parse the date entry into a tuple such as (6, 11, 2007)?

import csv

f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, float, str, str, float, float, float, float, int]
converted = [ func(val) for func, val in zip(types, row) ]

# Convert the date into a tuple of ints
converted[2] = tuple(int(a) for a in converted[2].split('/'))

record = dict(zip(headers, converted))
