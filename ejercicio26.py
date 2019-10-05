SEGUNDOS=int(input('ingresa los segundos:'))

segundos_x_dia=86400
segundos_x_hora=3600
segundos_x_minuto=60
segundos=SEGUNDOS


D=int(SEGUNDOS/segundos_x_dia)
segundos=segundos%segundos_x_dia

print('\n dias:',D)
print('segundos restantes',segundos)

H=int(segundos/segundos_x_hora)
segundos=segundos%segundos_x_hora

print('\n horas:',H)
print('segundos restantes',segundos)

M=int(segundos/segundos_x_minuto)
segundos=segundos%segundos_x_minuto

print('\n minutos:',M)
print('segundos restantes',segundos)

S=segundos

print('\n D:HH:MM:SS')
print('%d:%02d:%02d:%02d.' % (D,H,M,S) )