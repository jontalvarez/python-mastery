def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
            except ValueError as e:
                print('Couldn''t parse:', line)
                print('Failed : Reason', e)
            total_cost = total_cost + nshares * price

    return total_cost

if __name__ == '__main__':
    print(portfolio_cost('../Data/portfolio.dat'))