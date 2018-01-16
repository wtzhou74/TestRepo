# distribute functions into different files
# include another file / package
import tutorial16_subModule
import random
# use the function defined in other file
tutorial16_subModule.fish()
x = random.randrange(1,1000)
print(x)