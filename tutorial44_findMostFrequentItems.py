from collections import Counter

text = "Why don't you read the first row(0) cell values (0-n) " \
       "(aka column names) and put(columnName,columnIndex) into a map" \
       " of String/int. Then you can reference the column index by name."

words = text.split()    # split the string into list
# print(words)

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
