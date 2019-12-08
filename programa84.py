def mediana(a, b, c):
    if a < b and b < c or a > b and b > c:
        return b
    if b < a and a < c or b > a and a > c:
        return
    if c < a and b < c or c > a and b > c:
        return c

def alternarmediana(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

def main():
    x = float(input('Introduce el primer valor: '))
    y = float(input('Introduce el segundo valor: '))
    z = float(input('Introduce el tercer valor: '))

    print('El valor medio es ', mediana(x, y, z))
    print('Usando el metodo alternativo, esto es: ', alternarmediana(x, y, z))
main()