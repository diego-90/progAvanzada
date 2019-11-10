d = int(input('íntrodusca el dia:'))
m = input('introdusca el mes:')

if d==1 and m=='enero':
    print('anio nuevo')

elif d==16 and m=='septiembre':
    print('dia de la independencia')

elif d==25 and m=='diciembre':
    print('navidad')
else:
    print('no hay descanso')