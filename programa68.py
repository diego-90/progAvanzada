linea = input('Introduce 8 bits: ')

while linea != '':
    if linea.count('0') + linea.count('1') !=8 or len(linea) !=8:
        print('No son 8 bits')
    else:
        uno = linea.count('1')
        if uno % 2== 0:
            print('La paridad de bits deberia de ser 0.')
        else:
            print('La paridad de bits deberia de ser 1')
    linea = input('Introduce 8 bits: ')