# Random numbers
# To use random.seed for same number print


import random

random.seed(2)
print(random.random())


list_numbers = [22, 333, 34, 76, 8, 56, 827]
random.shuffle(list_numbers)
print(list_numbers)


