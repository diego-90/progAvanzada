from math import tan,pi
longuitud = int(input('ingrese la longuitud de cada lado del poligono:'))
numero = int(input('ingrese el numero de lados:'))
area = (numero*longuitud**2)/(4*tan(pi/numero))
print('el area del poligono es:',area)