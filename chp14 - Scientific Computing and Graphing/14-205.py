from matplotlib import pyplot as plt
from numpy import arange

plt.bar(arange(0, 10)*2, arange(1, 21, 2))
plt.bar(arange(0, 10)*2 + 1, arange(1, 31, 3), color="red")
plt.show()
