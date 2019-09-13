from matplotlib import pyplot as plt
from numpy import arange

x_points = arange(1, 21)
baseline = arange(0, 20)
plt.plot(x_points, baseline ** 2, "g-o", x_points, baseline, "r-^")
plt.axis([0, 21, 0, 400])
plt.title("Amount of Python learned over time")
plt.xlabel("Days")
plt.ylabel("Standardized knowledge index score")
plt.legend(("Real Python", "Other course"), loc=2)
plt.show()
