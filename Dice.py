import random


class Dice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice = Dice()
res = dice.roll()
print(res)




