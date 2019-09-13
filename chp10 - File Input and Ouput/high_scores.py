import csv
import os

my_path = "."

high_scores = {}

with open(os.path.join(my_path, "scores.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    for person, score in my_file_reader:
        if person in high_scores:
            if int(score) > high_scores[person]:
                high_scores[person] = int(score)
        else:
            high_scores[person] = int(score)

for p, s in sorted(high_scores.items()):
    print(p, s)

