# pcost.py
#
# Exercise 1.27

import csv, sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as portfolio:
        rows = csv.reader(portfolio)
        headers = next(rows)

        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except ValueError:
                print("Couldn't parse", row)
        
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost:', cost)
