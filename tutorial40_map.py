income = [10, 20, 43, 59, 10]

def double_money(dollars):
    return dollars * 2

# call the map function, P1-function, P2-item
new_income = list(map(double_money, income))
print(new_income)

# alternative way for map
# for item in income: