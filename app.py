""" from ecommerce.shipping import calc_shipping
# importing function from shipping without using . while calling
calc_shipping()
calc_shipping()
#from ecommerce import shipping
#call using
#shipping.calc_shipping() """

import random



class Dice:
    def roll(self):
        first = random.randint(1,6)
        return first

dice = Dice()
print(dice.roll())
