import csv
import os

my_path = "."

my_ratings = [["Movie", "Rating"],
    ["Rebel Without a Cause", "3"],
    ["Monty Python's Life of Brian", "5"],
    ["Santa Claus Conquers the Martians", "0"]]

with open(os.path.join(my_path, "movies.csv"), "w") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerows(my_ratings)