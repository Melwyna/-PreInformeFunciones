#Primero el usuario ingrese el valor de la variable#

num=int(input("Ingrese el numero:"))
#despues defini#
def numeros_primohermanos():
#hago un contador para contar los divisores#
 con=0
#hago un for con las condiciones correspondientes#
 for x in range(2,num+1):
  if num%x==0:
   con+=1
 if con>=3 and num%6==0 and num==6:
  print("El numero no es primo hermano")
 else:
  print("El numero es primo hermano")

numeros_primohermanos()
