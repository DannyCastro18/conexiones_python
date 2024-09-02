#operadores comparación

print(5 > 3)
print ('a' in "casa")

edad = 15
if (edad > 17):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#operadores lógicos

if 5 > 3 or 9 > 10:
    print("son mayores")
    print("5 es mayor que 3")
    
if True:
    pass
else:
    pass

#switch case

mes = 2
match(mes):
    case 1: print("Enero")
    case 2: print("Febrero")
    case _: print("Otro....")