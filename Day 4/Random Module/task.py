import random

heads = 'heads'
tails = 'tails'
my_random = random.randint(0,1)
if my_random == 1:
    print(heads)
elif my_random == 0:
    print(tails)