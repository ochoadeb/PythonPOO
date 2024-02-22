class Animal:
    def __init__(self, cant_patas, tipo):
        self.cant_patas = cant_patas
        self.tipo = tipo
    
    def comer(self):
        return "estoy comiendo"


class Perro(Animal):
    def __init__(self, cant_patas, tipo, nombre, raza):
        self.cant_patas = cant_patas
        self.tipo = tipo
        self.nombre = nombre
        self.raza = raza
    
    def correr(self):
        return "estoy corriendo"


class Aguila(Animal):
    def volar(self):
        return "estoy volando"
    
#test de la instancia de la clase

primer_animal = Animal(4, "vertebrado")
print("el primer animal es:", primer_animal)
