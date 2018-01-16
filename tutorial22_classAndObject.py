# Create a class
class Enemy:
    # variables
    life = 3

    # functions
    def attack(self):
        print("ouch!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

# Create object
# Each object is independent of each other
enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()