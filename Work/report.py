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