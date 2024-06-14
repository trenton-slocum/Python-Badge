import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/trent/Downloads/MSDS-Orientation-Computer-Survey(in).csv')

plt.hist(df['CPU Number of Cores (int)'])
plt.ylabel('Frequency')
plt.xlabel('CPU Number of Cores')
plt.show()