def calcular_hipotenusa (lado1,lado2):
    hipotenusa = (lado1**2 + lado2**2)**(0.5)
    return hipotenusa
L1 = float(input('inserta el lado 1: '))
L2 = float(input('inserta el lado 2: '))

hip = calcular_hipotenusa(L1,L2)
hip2 = calcular_hipotenusa(3.5,5.0)
print('La hipotenusa es: ', hip)
print('La hipotenusa es: ', hip2)