from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    # make a representation after init
    def __repr__(self):
        return self.name + ":" + str(self.user_id)

users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 65),
    User('Joby', 32)
]

# default order
for user in users:
    print(user)

print("---------")

# sorted by attribute name
for user in sorted(users, key=attrgetter('name')):
    print(user)
print("---------")

# sorted by attribute user_id
for user in sorted(users, key=attrgetter('user_id')):
    print(user)