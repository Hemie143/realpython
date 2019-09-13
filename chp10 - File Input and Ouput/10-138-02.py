import csv
import os

my_path = "."

cat_pastimes = []

with open(os.path.join(my_path, "pastimes.csv"), "r") as my_file:
    my_file_reader = csv.reader(my_file)
    next(my_file_reader)
    for row in my_file_reader:
        print(row)
        if row[1].lower().find('fighting') >= 0:
            row.append('Combat')
        else:
            row.append('Other')
        cat_pastimes.append(row)

print(cat_pastimes)


with open(os.path.join(my_path, "categorized pastimes.csv"), "w") as my_file:
    my_file_writer = csv.writer(my_file)
    my_file_writer.writerow(['Name', 'Favorite Pastime', 'Type of Pastime'])
    my_file_writer.writerows(cat_pastimes)

