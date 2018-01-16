# define a list
# item = ['December 23, 2015', 'Bread Gloves', 8.51]
# date = item[0]  # get the first item

# alternative way
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]
print(name)

# unknown list size
def drop_first_last(grades):
    first, *middle, last = grades # note the *middle
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 56, 89, 99, 100])