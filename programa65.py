from math import sqrt
perimetro = 0

x1 = int(input("Introduce la cordenada x: "))
y1 = int(input("Introduce la coordenada y: "))

x2 = x1
y2 = y1

line = input('Introduce la coordenada x, (blanco para quitar): ')
while line !='':
    x = float(line)
    y = float(input('Introuce la coordenada y: '))
    distancia = sqrt((x2-x)**2 + (y2-y)**2)
    perimetro = perimetro + distancia
    x2=x
    y2=y
    line= input('Inroduce la coordenada x, (blanco para quitar): ')
distancia = sqrt((x1-x)**2 + (y1-y)**2)
perimetro = perimetro + distancia
print('El perimetro del poligono es: ', perimetro)