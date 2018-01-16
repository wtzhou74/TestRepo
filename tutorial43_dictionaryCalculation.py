stocks = {
    'GOOG': 520.23,
    'FB': 76.43,
    'YAHOO': 39.23,
    'AMAZON': 309.90,
    'AAPL': 99.0
}

# print(min(stocks))  # sorted by KEY

# create a new list by Zip
# (520.23, GOOG) (76.43, FB)
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
