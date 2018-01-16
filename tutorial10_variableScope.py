
# outside functions
# a = 7823

def corn():
    # inside function, then only the function can use it
    a=1211
    print(a)


def fudge():
    print(a)

corn()
fudge()