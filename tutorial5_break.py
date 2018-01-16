magicNumber = 26
# String cannot align a number with "+" directly
# print(9, " Bucky")
for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number")
        break
    else:
        print(n)