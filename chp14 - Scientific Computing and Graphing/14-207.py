from matplotlib import pyplot as plt
from numpy import arange

plt.bar(arange(0, 10)*3, arange(1, 21, 2))
plt.bar(arange(0, 10)*3 + 1, arange(1, 31, 3), color="red")
plt.xticks(arange(0, 10)*3 + 1, arange(1, 11), fontsize=20)
plt.title("Coffee consumption due to sleep deprivation")
plt.xlabel("Group number")
plt.ylabel("Cups of coffee consumed")
plt.legend(("Control group", "Test group"), loc=2)
plt.show()
