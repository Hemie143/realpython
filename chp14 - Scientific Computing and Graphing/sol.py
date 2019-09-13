from matplotlib import pyplot as plt
import csv
import os
path = "./"

years = []
temperatures = []
pirates = []

with open(os.path.join(path, "pirates.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    # my_file_reader.next()  # skip header row
    next(my_file_reader)
    for year, temperature, pirate_count in my_file_reader:
        years.append(year)
        temperatures.append(temperature)
        pirates.append(pirate_count)

plt.plot(pirates, temperatures, "r-o")

# label graph
plt.title("Global temperature as a function of pirate population")
plt.xlabel("Total pirates")
plt.ylabel("Average global temperature (Celsius)")
plt.axis([-300, 48000, 14, 16])

# annotate points with years
for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temperatures[i]))

# save and display graph
plt.savefig(os.path.join(path, "pirates.png"))
plt.show()