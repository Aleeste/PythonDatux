
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena
 
persona1=Persona("Alejandra","Quiroz")
print(persona1)