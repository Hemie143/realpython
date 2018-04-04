user_string = input('Enter a string: ')
l = len(user_string)
if l < 5:
    print('The string length is less than 5 characters.')
elif l > 5:
    print('The string length is greater than 5 characters.')
else:
    print('The string length is equal to 5 characters.')