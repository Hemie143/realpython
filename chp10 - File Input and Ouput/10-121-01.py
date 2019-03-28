
my_output_file = open("hello.txt", "w")
lines_to_write = ["This is my file.", "\n There are many like it,", "\nbut this one is mine."]
my_output_file.writelines(lines_to_write)
my_output_file.close()

my_output_file = open("hello.txt", "a")
next_line = ["\nNON SEQUITUR"]
my_output_file.writelines(next_line)
my_output_file.close()

my_input_file = open("hello.txt", "r")
print(my_input_file.readlines())
my_input_file.close()

my_input_file = open("hello.txt", "r")
for line in my_input_file.readlines():
    print(line, end="")
my_input_file.close()

print()
my_input_file = open("hello.txt", "r")
line = my_input_file.readline()
while line != "":
    print(line, end="")
    line = my_input_file.readline()
my_input_file.close()

print()
with open("hello.txt", "r") as my_input_file:
    for line in my_input_file.readlines():
        print(line, end="")

with open("hello.txt", "r") as my_input, open("hi.txt", "w") as my_output:
    for line in my_input.readlines():
        my_output.write(line)

my_input_file = open("hello.txt", "rb")
print("Line 0 (first line):", my_input_file.readline())
my_input_file.seek(0)           # jump back to beginning
print("Line 0 again:", my_input_file.readline())
print("Line 1:", my_input_file.readline())
my_input_file.seek(8)           # jump to character at index 8
print("Line 0 (starting at 9th character):", my_input_file.readline())
my_input_file.seek(10, 1)       # relative jump forward 10 characters
print("Line 1 (starting at 11th character):", my_input_file.readline())
my_input_file.close()