calificaciones = []

while True:
    calificacion = input("Introduce la calificacion: ")

    puntos = 0

    if calificacion == "":
        break
    if calificacion == "A+":
        puntos = 4.0
    if calificacion == "A":
        puntos = 4.0
    if calificacion == "A-":
        puntos = 3.7
    if calificacion == "B+":
        puntos = 3.3
    if calificacion == "B":
        puntos = 3.0
    if calificacion == "B-":
        puntos = 2.7
    if calificacion == "C+":
        puntos = 2.3
    if calificacion == "C":
        puntos = 2.0
    if calificacion == "C-":
        puntos = 1.7
    if calificacion == "D+":
        puntos = 1.3
    if calificacion == "D":
        puntos = 1.0
    if calificacion == "F":
        puntos = 0
    
    calificaciones.append(puntos)

total = 0 
num = 0
for calificacion in calificaciones:
    total += calificacion 
    num += 1

promedio = total / num 

print("Tu promedio de calificaciones es: ",(promedio))