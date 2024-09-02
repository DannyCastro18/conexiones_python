#Hacer un programa que implemente una funcion que reciba como parametro una lista con numeros enteros y como resultado debe devolver la suma de los numeros 
def  sumaLista(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        suma += numero
    return suma

numeros = [1, 3, 4, 76]

sumaNumeros = sumaLista(numeros)

print(sumaNumeros)
