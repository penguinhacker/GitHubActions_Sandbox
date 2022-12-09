class Persona:
    def __init__(self,n,e):
        self.nombre = n
        self.edad = e

    def cumplirAnhos(self):
        self.edad +=1

    def cambiarNombre(self,n):
        self.nombre = n

