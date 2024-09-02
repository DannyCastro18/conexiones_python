vegetariana = ["Pimiento" , "Tofu"]
noVegetariana = ["Peperoni" , "Jamon", "Salmon"]

opcionPizza = int(input("tipo de Pizzas:\n1.Vegetariana\n2.No Vegetariana\n Selecciona Pizza:"))

if opcionPizza == 1:
    print("Ingredientes de la Pizza Vegetariana")
    print("1. ", vegetariana[0])
    print("2. ", vegetariana[1])
    ingrediente = int(input("Seleccione ingrediente: (1,2):"))
    ingredientesPizza = ["Tomate", "Mozarella", vegetariana[ingrediente-1]]
else:
    print("Ingredientes de la Pizza no Vegetariana")
    print("1. ", noVegetariana[0])
    print("2. ", noVegetariana[1])
    print("3. ", noVegetariana[2])
    ingrediente = int(input("Seleccione ingrediente: (1,2,3):"))
    ingredientesPizza = ["Tomate", "Mozarella", noVegetariana[ingrediente-1]]
    
print("Ingredientes de la pizza seleccionada\n", ingredientesPizza)