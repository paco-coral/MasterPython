#Ejercicio tienda de Libros
print("Proporciona los siguientes datos del Libro")
nomLibro = input("Ingrese el nombre del Libro : ")
idLibro = int(input("Ingrese el ID del Libro : ")) 
precio = float(input("Ingrese el precio : "))
envio = input("Envio Gratuito(True / False) : ")
if envio == "True":
    envio = True
else:
    envio = False
print("Nombre : ",nomLibro)
print("Id : ",idLibro)
print("Precio : ",precio)
print("Envio : ",envio)
print(type(envio))
