from operator import itemgetter

stocks = [
    {'ticker': 'GOOG', 'price': 520.23},
    {'ticker': 'APPL', 'price': 32.23},
    {'ticker': 'FB', 'price': 430.23},
    {'ticker': 'MSFT', 'price': 312.23},
    {'ticker': 'FB', 'price': 60.23}
]

# sorted by price
for x in sorted(stocks, key=itemgetter('price')):
    print(x)

print("--------------")

# sorted by ticker first, and then price
for x in sorted(stocks, key=itemgetter('ticker', 'price')):
    print(x)
