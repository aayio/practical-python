# pcost.py
#
# Exercise 1.27

import csv, sys, report

def portfolio_cost(filename):
    total_cost = 0.0

    # Initial implementation
    # with open(filename, 'rt') as portfolio:
    #     rows = csv.reader(portfolio)
    #     headers = next(rows)
        
    #     for rowno, row in enumerate(rows, start=1):
    #         record = dict(zip(headers, row))
    #         try:
    #             shares = int(record['shares'])
    #             price = float(record['price'])
    #             total_cost += shares * price
    #         except ValueError:
    #             print(f'Row {rowno}: Bad row: {row}')
    
    # with read_portfolio
    portfolio = report.read_portfolio(filename)
    
    for s in portfolio:
        total_cost += s.shares * s.price
    
    return total_cost

# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'

def main(argv):
    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
