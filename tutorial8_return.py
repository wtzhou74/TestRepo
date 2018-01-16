def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

bucky_limit = allowed_dating_age(27)
print("bucky limit date girls", bucky_limit, "or older")