class Tuna:

    # init belongs to class, the same as STATIC/ Constructor in Java
    def __init__(self):
        print("BLDAFDD")

    def swim(self):
        print('I am swimming')

flipper = Tuna()
flipper.swim()


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(10)
sandy = Enemy(19)

jason.get_energy()
sandy.get_energy()

