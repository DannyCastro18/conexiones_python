#pedir salario al usuario
salario = int(input ("Ingrese su salario: "))

if (salario < 1000000):
    impuesto = salario * 1/100
elif(salario>=1000000 and salario < 2000000):
    impuesto = salario * 3/100
elif(salario >= 2000000 and salario < 4000000):
    impuesto = salario * 5/100
elif(salario >= 4000000 and 10000000):
    impuesto = salario * 7/100
else:
    impuesto = salario *10/100
    
#mostrar resultados
print(f"De acuerdo a su salario de {salario} el impuesto a pagar es: {impuesto}")