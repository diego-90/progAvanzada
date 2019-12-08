resultado = ''
q = int(input('Inserta el numero:  '))


r = q % 2

resultado = str(r) + resultado
q = q // 2


while q > 0:
    r = q % 2
    resultado = str(r) + resultado
    q = q // 2 

print('binaro', resultado)

