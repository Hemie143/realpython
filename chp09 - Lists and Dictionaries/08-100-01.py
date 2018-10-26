
def enrollment_stats(universities):
    students_count = [u[1] for u in universities]
    fees = [u[2] for u in universities]
    return (students_count, fees)


def sum(l):
    l_sum = 0
    for x in l:
        l_sum += x
    return l_sum


def mean(l):
    return sum(l)/len(l)     # Assume list isn't empty


def median(l):
    n = len(l)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(l)[n // 2]
    else:
        return sum(sorted(l)[n // 2 - 1:n // 2 + 1]) / 2.0


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]


population_list, fees_list = enrollment_stats(universities)
print('*'*20)
print('Total students:   {}'.format(sum(population_list)))
print('Total tuition:  $ {}'.format(sum(fees_list)))
print()
print('Student mean:     {}'.format(int(mean(population_list))))
print('Student median:   {}'.format(median(population_list)))
print()
print('Tuition mean:   $ {}'.format(int(mean(fees_list))))
print('Tuition median: $ {}'.format(median(fees_list)))
print('*'*20)