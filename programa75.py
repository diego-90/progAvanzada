n = int(input('Introduce un numero entero pocitivo: '))

m = int(input('Introduce un numero entero pocitivo: '))

d = min(n,m)

while n % d !=0 or m % d != 0:
    d = d-1
print('El maximo divisor comun de ', n, 'y ', m,'es:',d )