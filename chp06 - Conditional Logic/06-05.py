number = None
while not number:
    try:
        number = int(input('Enter an integer: '))
    except ValueError:
        print("try again")

print('The number is {}'.format(number))