masa = float (input('inserte su masa en kg:'))
estatura = float(input('inserta tu estatura en metros:'))
imc= masa / estatura**2

if imc < 16 :
 print('tienes delgades severa')
elif imc >= 16 and imc <17:
 print('tienes delgades moderado')
elif imc >= 17 and imc <18.5:
 print ('tienes delgades leve')
elif imc >= 18.5 and imc <25:
 print('tienes un estado normal')
elif imc  >=25 and imc <30:
 print('tienes preobesidad')
elif imc >=30 and imc <35:
 print('tienes obesidad leve')
elif imc >=35 and imc <40:
 print('tienes obesidad media')
elif imc >=40:
 print('tienes obesidad morbida')
else:
 print('opcion invalida')
print('su imc fue de', imc)
