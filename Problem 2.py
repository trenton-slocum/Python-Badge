import numpy as pd
import matplotlib as plt
import pandas as pd

fib = [0, 1]
key = True

while key == True:
    f = fib[-1] + fib[-2]
    if f < 4000000:
        fib.append(f)
    else:
        key = False

fib_even = []

for i in fib:
    if i % 2 == 0:
        fib_even.append(i)

print(sum(fib_even))