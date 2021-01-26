#Ejercicio Operadores Aritmeticos
alto = int(input("Proporciona el Alto : "))
ancho = int(input("Proporciona el Ancho : "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area = ",area)
print("Perimetro = ",perimetro)

#Ejercicio Operadores Logicos
num1 = int(input("Ingresa el primer numero : "))
num2 = int(input("Ingresa el segundo numero : "))
if (num1 > num2):
    print("El numero mayor es: ",num1)
elif (num2 > num1):
    print("El numero mayor es: ",num2)
else:
    print(num1," Es Igual a ", num2)