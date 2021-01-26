#Ejercicio AND
print("Comparar si un numero esta dentro del rango del 1 - 10")
#Variables a utilizar
a = int(input("Ingrese un numero : "))
vMinimo = 0
vMaximo = 10
#Operador Logico (AND)
rango = (a >= vMinimo) and (a <= vMaximo)
if rango:
    print("Dentro de Rango")
else:
    print("Fuera de Rango")                     
    
#Ejercicio OR
print()
print("Saber si puedes ir al Parque")
vacaciones = False
diaDescanso = True
if (vacaciones or diaDescanso):
    print("Puedes ir al Parque")
else:
    print("Tienes deberes que hacer")
    
#Ejercicio NOT
print()
print("Operador Logico Not")
variable = True
print ("La variable es : ", variable)
print ("La variable invertida es : ", not(variable))