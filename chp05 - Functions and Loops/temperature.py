
def C_to_F(temp):
    return temp*9/5+32

def F_to_C(temp):
    return (temp-32)*5/9

print('{} degrees F = {} degrees C'.format(72, F_to_C(72)))
print('{} degrees C = {} degrees F'.format(37, C_to_F(37)))
