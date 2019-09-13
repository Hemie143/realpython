import csv
import os

my_path = "."

with open(os.path.join(my_path, "tabbed wonka.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file, delimiter="\t")
    next(my_file_reader)
    for row in my_file_reader:
        print(row)