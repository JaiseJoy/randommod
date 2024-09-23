import random
from random import uniform, sample, choice

var = random.randint(1,7)

print(var)

random_var = random.random()
print(random_var)

random_range_var = random.randrange(1,20,2)
print(random_range_var)

uniform_random_var = random.uniform(3,5)
print(uniform_random_var)

sample_list = [1,2,3,4,5]

choice_variable = random.choice(sample_list)

print(choice_variable)