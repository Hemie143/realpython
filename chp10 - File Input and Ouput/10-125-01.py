f = open("poem.txt", "r")
for line in f.readlines():
    print(line)
f.close()

with open("poem.txt", "r") as poem:
    for line in poem.readlines():
        print(line)

with open("poem.txt", "r") as poem, open("output.txt", "w") as out:
    for line in poem.readlines():
        out.write(line)

with open("output.txt", "a") as out:
    out.write("\nan additional line of your choice")

