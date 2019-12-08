cargos = []

while True:
    edad = input("Introduzca la edad del huésped: ")

    if edad == "":
        break

    cargo = 0
    edad_int = int(edad)
    if edad_int <= 2:
        cargo = 0
    elif edad_int >= 3 and edad_int < 13:
        cargo = 14
    elif edad_int >= 65:
        cargo = 18
    else:
        cargo = 23
    cargos.append(cargo)

total = 0.00
for cargo in cargos:
    total += cargo

print("El total del grupo es:  $",(total))
