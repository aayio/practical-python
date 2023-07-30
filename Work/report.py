# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''opens a given portfolio file and reads it into a list of dictionaries'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
    
        for row in rows:
            holding = { 'name': row[0], 'shares': int(row[1]), 'price': float(row[2]) }
            portfolio.append(holding)
    
    return portfolio

def read_prices(filename):
    '''reads a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices'''
    prices = { }
    
    with open(filename, 'rt') as f:
        # this file does not have a header
        
        rows = csv.reader(f)
        
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Couldn't parse", row)
    
    return prices

# Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost = 0.0
current_value = 0.0

for s in portfolio:
    total_cost += s['shares'] * s['price']
    current_value += s['shares'] * prices[s['name']]

print(f'Current value of portfolio: {current_value:0.2f}')
print(f'Change: {current_value - total_cost:0.2f}')