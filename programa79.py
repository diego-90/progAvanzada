from random import randrange

piezas = 100
mx_value = randrange(1, piezas + 1)
print(mx_value)

num_updates = 0

for i in range(1, piezas):
    current = randrange(1, piezas + 1)
    if current > mx_value:
        mx_value = current
        num_updates = num_updates + 1
        print(current, '<== Update')
    else:
        print(current)
print('el valor máximo encontrado es:', mx_value )
print('el valor máximo fue actualizar es: ', num_updates, 'veces')