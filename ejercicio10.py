

from math import log
a = int(input('inserte el valor de a: '))

b = int(input('inserte el valor de b: '))
print('')
print(a, '+', b, 'es:                  ', a+b)
print('')
print(a, '-', b, 'es:                  ', a-b)
print('')
print(a, '*', b, 'es:                  ', a*b)
print('')
print(a, '/', b, 'es:                  ', a/b)
print('')
print(a, '%', b, 'es:                  ', a%b)
print('')
print('El logaritmo para', a, 'es:     %.2f' % log(a))
print('')
print(a, '^', b, 'es:                  ', a**b)