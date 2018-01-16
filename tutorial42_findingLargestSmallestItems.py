 package used to sort stuff easily
import heapq

grades = [32, 23, 34, 90, 54, 32, 43, 80, 9]
print(heapq.nlargest(3, grades)) # get the top 3 largest items

# dictionary
stocks = [
    {'ticker': 'GOOG', 'price': 520.23},
    {'ticker': 'APPL', 'price': 32.23},
    {'ticker': 'FB', 'price': 430.23},
    {'ticker': 'MSFT', 'price': 312.23}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))
