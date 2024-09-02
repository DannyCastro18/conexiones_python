palabras = []

for i in range(10):
    palabra = str(input("Ingresa una palabra: "))
    palabras.append(palabra)
    
busqueda = input("Ingrese la palabra: ")

cantidad = palabras.count(busqueda)

print(f"La palabra {busqueda} aparece {cantidad} veces en la lista \n {palabras} ")

#Solucion II

# cantidad=0
# for palabra in palabras:
#     if palabra==busqueda:
#         cantidad+=1