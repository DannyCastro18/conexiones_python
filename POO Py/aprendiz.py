from persona import Persona

class Aprendiz(Persona):
    def __init__(self, puntajeIcfes:int = 0, identificacion: str="15", nombre: str="Juan", correo: str="juanse@gmail.com")->None:
         super().__init__(identificacion, nombre, correo)
         self.__puntajeIcfes = puntajeIcfes
         
    
    def getPuntajeIcfes(self)->int:
        return self.__puntajeIcfes
    
    def setPuntajeIcfes(self, puntaje)->None:
        self.__puntajeIcfes = puntaje
         

    def saludar(self)->None:
        print(f"Desde Aprendiz. Hola soy un objeto de tipo {
            type(self).__name__}")