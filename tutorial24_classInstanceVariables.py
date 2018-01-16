class Girl:

    gender = 'female'   # default value, shared with all objects

    def __init__(self, name):
        self.name = name    # each object will have a different name

r = Girl('Rachel')
s = Girl('Stanky')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)