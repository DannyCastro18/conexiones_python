import math
def areaCuadrado(lado:float)->float:
    return lado*lado

def areaCirculo(radio:float)->float:
    return math.pi * radio **2

def areaTriangulo(base:float, altura:float)->float:
    return base*altura/2

areaC = areaCuadrado(5)
areaR = areaCirculo(3.8)
areaT = areaTriangulo(5.3,8.5)

print(f"El área del cuadrado con lado 5.8 es {areaC}")
print(f"El área del circulo con radio {3.8} es {areaR}")

def operaciones():
    x=5
    y=8
    
opera = operaciones()
print(opera)