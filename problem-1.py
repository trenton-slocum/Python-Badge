import numpy as np
import matplotlib as mp
import pandas as pd

multiples_three = []
multiples_five = []

for i in range(1000):
    if (i/3).is_integer() == True:
        multiples_three.append(i)

    if (i/5).is_integer() == True:
        multiples_five.append(i)

sum = 0

for i in multiples_three:
    sum += i

for i in multiples_five:
    if i not in multiples_three:
        sum += i

print(sum)