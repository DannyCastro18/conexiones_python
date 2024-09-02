class Animal():
    def __init__(self, peso:float) -> None:
        self.peso=peso
        
    def respirar(self)->None:
        print(f"{type(self).__name__}está respirando")
        
    
class Pez (Animal):
    
    def __init__(self, peso: float) -> None:
        super().__init__(peso)
        
    def nadar(self)->None:
        print("Nemo está nadando")
    
class Gato(Animal):
    
    def __init__(self, peso: float) -> None:
        super().__init__(peso)
        
    def maullar (self)->None:
        print("Tom está maullando")
        
class Perro(Animal):
    
    def __init__(self, peso: float) -> None:
        super().__init__(peso)
        
    def ladrar (self)->None:
        print("Lucas está Ladrando")