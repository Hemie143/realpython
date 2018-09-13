
def invest(amount, rate, time):
    print('principal amount: ${}'.format(amount))
    print('annual rate or return: {}'.format(rate))
    cap = amount
    for y in range(time):
        amount *= (1+rate)
        print('year {}: ${}'.format(y+1, amount))

invest(100, .05, 8)
invest(2000, .025, 5)