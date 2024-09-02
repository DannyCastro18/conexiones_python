# Para atributos privados
class Persona():
    def __init__(self, identificacion: str="15", nombre: str="Juan", correo: str="juanse@gmail.com")-> None:
        self.__identificacion =  identificacion
        self.__nombre =  nombre
        self.__correo = correo
    
    def getIdentificacion(self)->str:
        return self.__identificacion
    
    def getNombre(self)->str:
        return self.__nombre
    
    def getCorreo(self)->str:
        return self.__correo
    
    def setIdentificacion(self, identificacion)->None:
        self.__identificacion = identificacion
        
    def setNombre(self, nombre)->None:
        self.__nombre = nombre
        
    def setCorreo(self, correo)->None:
        self.__correo = correo