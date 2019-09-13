import csv
import os
my_path = "."
with open(os.path.join(my_path, "wonka.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    for row in my_file_reader:
        print(row)