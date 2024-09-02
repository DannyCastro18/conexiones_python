#Hacer un programa que lea un número entero y como resultado mostrar su correspondiente en notación binaria

numero = int(input("Ingrese número entero para obtener su binario: "))

binario = ''
numeroIngresado = numero
while(True):
    resultado = numero // 2
    residuo = numero % 2
    binario = str(residuo) + binario  #str lo convierte a string
    if(resultado == 1):
        binario = str(resultado) + binario 
        break 
    numero = resultado

print("Binario resultante: " , binario)
# print("")

# for i in range(len(binario), -1, -1, -1):
#     print(binario[i], end="")
    