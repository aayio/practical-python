# pcost.py
#
# Exercise 1.27

total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as portfolio:
    headers = next(portfolio)

    for line in portfolio:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        total_cost += shares * price
    
    print(f'Total cost {total_cost:.2f}')