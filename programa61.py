a = 1
sumatoria = 0
i = 0
while a !=0:
    a = int(input('Inserte un valor: '))
    sumatoria = sumatoria + a
    i = i + 1
promedio = sumatoria / (i-1)
print('El promedio es', promedio)
