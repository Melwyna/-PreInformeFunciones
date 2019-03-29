#primero defini#
def elevar_numero():


#luego coloque las variables a utilizar para que el usuario les escribiera el respectivo valor a cada una#

 a=float(input("Ingresa el numero a elevar: "))
 b=float(input("Ingresa el numero al que vas a elevar el numero anterior: "))
 c=float(input("Ingresa el numero a elevar: "))
 d=float(input("Ingresa el numero al que vas a elevar el numero anterior: "))

 res1=(a**b)
 res2=(c**d)

#y le coloque las respectivas condiciones#
 if res1>res2:
  print("El resultado del primer numero elevado es mayor:", res1, "> " , res2 )
 else:
  print("El resultado del segundo numero elevado es mayor", res2, "> " , res1 )

elevar_numero()