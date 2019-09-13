from matplotlib import pyplot as plt
from numpy import random

plt.hist(random.randn(10000), 20)
plt.annotate(r"$\hat \mu = 0$", xy=(0, 0), xytext=(0, 300), ha="center",
             arrowprops=dict(facecolor='black'), fontsize=20)
plt.show()
