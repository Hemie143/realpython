from matplotlib import pyplot as plt
from numpy import arange

plt.bar(arange(0, 10)*3, arange(1, 21, 2))
plt.bar(arange(0, 10)*3 + 1, arange(1, 31, 3), color="red")
plt.xticks(arange(0, 10)*3 + 1, arange(1, 11), fontsize=20)
plt.show()
