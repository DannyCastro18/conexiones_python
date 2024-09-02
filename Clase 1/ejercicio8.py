#funciones

def sumar (x,y):
    return x+y

suma = sumar(5,3)
print(suma)

def mostrarDatos(nombre="Maria", apellido="Salazar"):
    print(nombre, apellido)
    
mostrarDatos()

mostrarDatos(nombre="Rocio")
mostrarDatos(apellido="Castro", nombre= "Martin")

def obtenerCiudad(ciudad:str)->str:
    return ciudad

ciudad = obtenerCiudad("Medellín")
print(ciudad)
