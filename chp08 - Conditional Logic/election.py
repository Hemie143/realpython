import random

region1_chance = 0.87
region2_chance = 0.65
region3_chance = 0.17

votes = 10000

countA = 0

for t in range(votes):
    winA = 0
    if random.random() < region1_chance:
        winA += 1
    if random.random() < region2_chance:
        winA += 1
    if random.random() < region3_chance:
        winA += 1
    if winA > 1:
        countA += 1

print("Probability Win A: {}".format(countA/votes))
print("Probability Win B: {}".format((votes-countA)/votes))