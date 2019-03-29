#Primero el usuario ingrese el valor de la variable#

num=int(input("Ingrese el numero:"))
#despues defini#
def numeros_primos():
#hago un contador para contar los divisore#
 con=0
#hago un for con las condiciones correspondientes#
 for x in range(2,num+1):
  if num%x==0:
   con+=1
 if con>=3:
  print("El numero no es primo")
 else:
  print("El numero es primo")

numeros_primos()
