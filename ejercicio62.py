print('precio original | descuento | precio total')
print('******************************************')
precio_original = 4.95
while precio_original <= 24.95:
    descuento = precio_original * 0.60
    precio_final = precio_original - descuento
    print('$%.2f''   |' %precio_original, '$%.2f''   |' %descuento, '$%.2f' %precio_final)
    precio_original = precio_original + 5