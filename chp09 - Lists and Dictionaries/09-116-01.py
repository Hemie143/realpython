cats = [0] * 100

for i in range(0, 100):
    for j in range(0, 100, i+1):
        cats[j] = -cats[j] + 1

for i, c in enumerate(cats):
    if c == 1:
        print(f'Cat {i+1}')

