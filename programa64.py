suma = 0
sumaredondeada = 0

interrumpido = False 
while not interrumpido:
	precio = input("Introduce el precio: ")
	
	if precio != "":
		precio = float(precio)
	else:
		break
		
	suma += precio 
	
	penique = precio * 100
	recorda = penique % 5
	
	if recorda > 2.5:
		penique += 5 - recorda 
	else:
		penique -= recorda 
	
	redondeado = penique * 0.01
	sumaredondeada += redondeado

print("El costo actual es: %.2f" %(suma))
print("Pagando en efectivo: %.1f" %(sumaredondeada))
