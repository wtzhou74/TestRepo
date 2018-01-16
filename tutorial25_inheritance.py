# inheritance: getting something from someone else

class Parent():

    def print_last_name(self):
        print('Roberts')

# inheritance
class Child(Parent):

    def print_first_name(self):
        print('Bucky')

    # override print_last_name function
    def print_last_name(self):
        print('Snitzleberg')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()