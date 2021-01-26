#Variables a Utilizar
a = 3
b = 2
print("Variable a = ",a)
print("Variable b = ",b)

#Operador de igualdad
resultado = (a == b)
print("Operador Igualdad (a == b) = ",resultado)

#Operador de Diferente
resultado = (a != b)
print("Operador Diferente (a != b) = ",resultado)

#Operador Mayor
resultado = (a > b)
print("Operador Mayor (a > b) = ",resultado)

#Operador Menor
resultado = (a < b)
print("Operador Menor (a < b) = ",resultado)

#Operador Mayor o Igual
resultado = (a >= b)
print("Operador Mayor o Igual (a >= b) = ",resultado)

#Operador Menor o Igual
resultado = (a <= b)
print("Operador Menor o Igual (a <= b) = ",resultado)


#Ejercicio
print();
print("Comprobar las variables a y b son pares o impares")

#Comprobamos la Variable A
if a % 2 == 0:
    print("La Variable (A) es par")
else:
    print("La Variable (A) es inpar")

#Comprobamos la Variable B
if b % 2 == 0:
    print("La Variable (B) es par")
else:
    print("La Variable (B) es inpar")
    
#Ejercicio 2
print();
print("Comprobamos si la variable edad es mayor de edad")
edad = 24
mEdad = 18
print("La edad es: ",edad)
if edad >= mEdad:
    print("Es Mayor de Edad")    
else:
    print("Es Menor de Edad")    