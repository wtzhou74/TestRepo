# dictionary KEY:VALUE
stocks = {
    'GOOG': 520.23,
    'FB': 76.43,
    'YAHOO': 39.23,
    'AMAZON': 309.90,
    'AAPL': 99.0
}

# Zip function to tie two lists together
minStock = min(zip(stocks.values(), stocks.keys()))
maxStock = max(zip(stocks.values(), stocks.keys()))
sortStock = sorted(zip(stocks.values(), stocks.keys())) # sorted by VALUE
print(minStock)
print(maxStock)
print(sortStock)