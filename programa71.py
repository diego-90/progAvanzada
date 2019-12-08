
import math
def main():
   
  #Input
  x = eval(input("\n Introduzca la raiz cuadrada: "))
  conjetura = eval(input("¿Cuál es tu conjetura?: "))
  #formula
  ans = x ** 1/2
  
  newt = (conjetura + (x / conjetura)) / 2 
  aprox = math.sqrt(x) - newt
  
  #output
  print("\n La raiz cuadra de ", x,"es: ", newt)
  print("la fórmula es", aprox,"precisa")

main()
