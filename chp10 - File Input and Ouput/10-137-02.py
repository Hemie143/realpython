import csv
import os

my_path = "."

with open(os.path.join(my_path, "movies.csv"), "w") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerow(["Movie", "Rating"])
    my_file_writer.writerow(["Rebel Without a Cause", "3"])
    my_file_writer.writerow(["Monty Python's Life of Brian", "5"])
    my_file_writer.writerow(["Santa Claus Conquers the Martians", "0"])