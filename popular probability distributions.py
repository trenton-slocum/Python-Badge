import matplotlib.pyplot as plt
import numpy as np

#Normal
mu, sigma = 0, 0.1
s = np.random.default_rng().normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, density = True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2)), linewidth =  2, color = 'g')
plt.show()

#Poisson
rng = np.random.default_rng()
s = rng.poisson(5, 1000)
count, bins, ignored = plt.hist(s, 14, density = True)
plt.show()

#Uniform
s = np.random.default_rng().uniform(-1, 0, 1000)
count, bins, ignored = plt.hist(s, 15, density = True)
plt.plot(bins, np.ones_like(bins), linewidth = 2, color = 'g')
plt.show()