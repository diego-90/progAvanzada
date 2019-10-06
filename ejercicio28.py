wc_offset = 13.12
wc_factor1 = 0.6215
wc_factor2 = -11.37
wc_factor3 = 0.3956
wc_exponent = 0.6
temperatura = int(input('introduce la temperatura del aire en Celsius:'))
velocidad = int(input('introduce la velocidad del viento en kilometros por hora:'))
wc1 = wc_offset + \
      wc_factor1*temperatura + \
      wc_factor2*velocidad**wc_exponent + \
      wc_factor3*temperatura*velocidad**wc_exponent
print('el índice de sensación térmica es, redondeado:',wc1) 