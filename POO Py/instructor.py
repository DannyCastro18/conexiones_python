from persona import Persona

class Instructor(Persona):
    
    def __init__(self, especialidad: str="Software", identificacion: str="15", nombre: str="Juan", correo: str="juanse@gmail.com")->None:
        super().__init__(identificacion, nombre, correo)
        self.__especialidad = especialidad
        
    def getEspecialidad(self)->str:
        return self.__especialidad
    
    def setEspecialidad(self, especialidad)->None:
        self.__especialidad = especialidad 
        
    def saludar(self)->None:
        print(f"Desde Instructor. Hola soy un objeto de tipo {
            type(self).__name__}")