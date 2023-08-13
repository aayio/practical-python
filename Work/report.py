# report.py
#
# Exercise 2.4

import csv, stock, tableformat
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    opens a given portfolio file and reads it into a list of dictionaries
    '''
    # Initial implementation
    # portfolio = []

    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)

    #     for row in rows:
    #         record = dict(zip(headers, row))
    #         holding = { 'name': record['name'], 'shares': int(record['shares']), 'price': float(record['price']) }
    #         portfolio.append(holding)
    
    # Use parse_csv
    with open(filename) as f:
        portfolio_as_dict = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
        portfolio_as_instances = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portfolio_as_dict ]

    return portfolio_as_instances

def read_prices(filename):
    '''
    reads a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices
    '''

    # Initial implementation
    # prices = { }
    
    # with open(filename, 'rt') as f:
    #     # this file does not have a header
        
    #     rows = csv.reader(f)
        
    #     for row in rows:
    #         try:
    #             prices[row[0]] = float(row[1])
    #         except IndexError:
    #             print("Couldn't parse", row)
    
    # Use parse_csv
    with open(filename) as f:
        prices = dict(parse_csv(f, types=[str, float], has_headers=False))
    
    return prices

def make_report(portfolio, prices):
    report = []
    
    for holding in portfolio:
        change = prices[holding.name] - holding.price
        row = (holding.name, holding.shares, prices[holding.name], change)
        report.append(row)
    
    return report

def print_change(portfolio, prices):
    total_cost = 0.0
    current_value = 0.0

    for s in portfolio:
        total_cost += s.shares * s.price
        current_value += s.shares * prices[s.name]

    print(f'Current value of portfolio: {current_value:0.2f}')
    print(f'Change: {current_value - total_cost:0.2f}')

def print_report(report, formatter):
    # Use a TableFormatter object
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    
    # This was the previous code for generating the header
    # header_string = '%10s %10s %10s %10s' % headers

    # My way of doing this is super hacky!
    # column_width = 10
    # num_columns = len(headers)
    # separator_string = ' '.join([column_width * '-'] * num_columns)

    # This is how dabeaz prints the separator string:
    # print(('-' * 10 + ' ') * len(headers))

    # print(header_string)
    # print(separator_string)
    
    ### End header generating code ###

    # Print report using old-style string formatting
    # for r in report:
    #     print('%10s %10d %10.2f %10.2f' % r)

    for name, shares, price, change in report:
        # Print report using f-strings        
        # price_str = f'${price:.2f}'
        # print(f'{name:>10s} {shares:>10d} {price_str:>10} {change:>10.2f}')
        
        # Use a TableFormatter object to print the rows
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
        
def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    
    # print_change(portfolio, prices)

    report = make_report(portfolio, prices)
    
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    
def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    if len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

if __name__ == '__main__':
    import sys
    main(sys.argv)
