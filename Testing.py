from RandomClass import *

a = Persona("pepe",15)

assert a.nombre == "pepe"

assert a.edad == 15

a.cumplirAnhos()

assert a.edad == 16

assert a.edad == 15
