from capitals import capitals_dict
import random

state = random.choice(list(capitals_dict))
capital = capitals_dict[state]

while True:
    response = input(f'What is the capital of {state} ? ')
    if response == capital:
        print('Correct')
        exit()
    if response == 'exit':
        print('Goodbye')
        exit()
