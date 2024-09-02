#estructuras Repetitivas

for i in range(3,14,2): #primer elemento desde donde inicia, segundo elemento donde llega menos 1, tercer elemento como se cuenta en este caso de 2 en 2 
    print(i)

for i in range(1,11): #primer elemento desde donde inicia, segundo elemento donde llega menos 1 
    print(i)

for i in range(3): #primer elemento desde donde inicia
    for j in range(3):
        print(i, j)
        
ciudades = ["Cali", "Popayan", "Neiva", "Barranquilla"]

for ciudad in ciudades:
    print(ciudad)
    longitudCiudad = len(ciudad)
    print(f"Longitud: {longitudCiudad}")    
    
for i in range(len(ciudades)):
    print(ciudades[i])
    
posCali = ciudades.index("Cali")
print(posCali)

#while


i = 0
while(i>10):
    print(i)
    i += 1
else:
    print("No ingresaste")
    
while(True):
    print("Hola")
    x = 5
    if x == 5:
        break #sacar de una estructura repetitiva