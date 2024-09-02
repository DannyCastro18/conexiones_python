# creación de clases, constructores y métodos
class Perro():
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        
    def ladrar(self):
        print(f"{self.nombre}:¡Guau! ¡Guau! ¡Guau!")
        
    def caminar(self, pasos):
        print(f"{self.nombre} está caminando {pasos} pasos")
        
