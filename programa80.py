import random



def coin_flipper():
    
    opcion = ['S', 'C']
    vueltas = ''
    
    while True:
        vuelta = random.choice(opcion)
        vueltas = vueltas + vuelta
        
        if len(vueltas) >= 3:
            if ( vueltas[-3] == vueltas[-2] == vueltas[-1] ):
                break
            else:
                continue
    return vueltas




resultado = []
suma = 0

for i in range(10):
    resultado.append(coin_flipper())
    suma += len(resultado[i])
    print(resultado[i], "(%d)" %len(resultado[i]))

vueltasprom = suma/10    

print ("En promedio %d vueltas" %vueltasprom)
