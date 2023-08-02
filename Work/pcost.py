# pcost.py
#
# Exercise 1.27

import csv, sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as portfolio:
        rows = csv.reader(portfolio)
        headers = next(rows)
        
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost:', cost)
