dias = float(input('introdusca los dias:'))
horas = float(input('introdusca las horas:'))
minutos = float(input('introdusca los minutos:'))
segundos = float(input('introdusca los segundos:'))
D=dias*86400
H=horas*3600
M=minutos*60
s=segundos
totaldesegundos=D+H+M+s
print('el total de segundo es:',totaldesegundos)