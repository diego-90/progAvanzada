import math


V0=float(input('ingresa la velocidad inicial:'))
g=float(input('ingresa la gravedad:'))
d=float(input('ingresa la distancia:'))


Vf=math.sqrt(V0*V0)+math.sqrt(2*g*d)

print('la velocidad final es:', Vf,'m/s')