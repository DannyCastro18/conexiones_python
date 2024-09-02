#Hacer un programa que almacene la edad de 5 personas. Al final mostrar por pantalla la menor y mayor edad registrada

edades = []

for i in range(5):
    edad = int(input("Ingresa tu edad: "))
    edades.append(edad)
    
menor = min(edades)
mayor = max(edades)
print(f"La edad mayor es: {mayor}")
print(f"La edad menor es: {menor}")