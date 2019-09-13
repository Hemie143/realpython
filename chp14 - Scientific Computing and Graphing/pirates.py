import csv
import os
from matplotlib import pyplot as plt

years = []
temps = []
pirates = []

path = "./"
with open(os.path.join(path, "pirates.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)
    for year, temp, pirate in my_file_reader:
        years.append(year)
        temps.append(temp)
        pirates.append(pirate)

plt.plot(pirates, temps)
plt.title("Temperature vs Number of pirates ")
plt.xlabel("Number of pirates")
plt.ylabel("Temperature (° Celsius)")

# plt.axis([0, 48000, 14, 16])

# annotate points with years
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temps[i]))

plt.savefig(path + "pirates.png")
plt.show()

