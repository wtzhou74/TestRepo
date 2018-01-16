class Mario():
    def move(self):
        print('I am moving!')

class Shroom():
    def eat_shroom(self):
        print('Now I am big')

# class which inherit both class
class BigMario(Mario, Shroom):
    pass    # do nothing

bm = BigMario()
bm.move()
bm.eat_shroom()