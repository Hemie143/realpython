birthdays = {}
birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

if not 'Yoda' in birthdays:
    birthdays['Yoda'] = 'unknown'
if not 'Darth Vader' in birthdays:
    birthdays['Darth Vader'] = 'unknown'

for n in birthdays:
    print(f'{n} {birthdays[n]}')

del(birthdays['Darth Vader'])
birthdays = dict([('Luke Skywalker', '5/24/19'), ('Obi-Wan Kenobi', '3/11/57'), ('Darth Vader', '4/1/41')])
print(birthdays)