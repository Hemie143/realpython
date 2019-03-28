desserts = ['ice cream', 'cookies']
desserts.sort()
print(desserts)
print(desserts.index('ice cream'))
food = desserts[:]
food.append('broccoli')
food.append('turnips')
print('desserts: {}'.format(desserts))
print('food    : {}'.format(food))
food.remove('cookies')
print('food    : {}'.format(food[0:2]))
breakfast = 'cookies, cookies, cookies'.split(', ')
print('breakfast: {}'.format(breakfast))

def filter_1_20(l):
    # return list(filter(lambda x: 1 <= x <= 20, l))
    return [x for x in l if 1 <= x <= 20]

print(filter_1_20([2, 4, 8, 16, 32, 64]))