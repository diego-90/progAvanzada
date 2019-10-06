MENOS_DEPOSITADO = 0.10
MAS_DEPOSITADO = 0.25
menos = int(input('¿cuantos recipientes tienen 1 litro o menos?:'))
mas = int(input('¿cuantos recipientes tienen mas de 1 litro?:'))
reembolso = menos * MENOS_DEPOSITADO * MAS_DEPOSITADO
print('su reembolso total será ', reembolso)