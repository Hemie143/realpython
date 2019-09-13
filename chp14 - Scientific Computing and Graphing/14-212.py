from matplotlib import pyplot as plt
from numpy import random

plt.hist(random.randn(10000), 20)
path = "./"
plt.savefig(path + "histogram.png")
plt.savefig(path + "histogram.pdf")

