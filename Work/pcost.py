# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as portfolio:
        headers = next(portfolio)

        for line in portfolio:
            try:
                row = line.split(',')
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except ValueError:
                print("Couldn't parse", line)
        
        return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
