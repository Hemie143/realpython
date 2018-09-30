from random import randint

throws = 10000

avg = 0

for t in range(throws):
    toss = randint(1, 6)
    avg = (avg * t + toss) / (t + 1)

print('average: {}'.format(avg))