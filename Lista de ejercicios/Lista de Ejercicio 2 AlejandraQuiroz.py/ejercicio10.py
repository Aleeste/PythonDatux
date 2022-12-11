# Definir los atributos y metodos de una de las siguiente clases#
# personas#
# gato#
# producto

class Persona:
    def __init__(self,nombre,apellido,direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
    
    def saludar(self):
        print(f"¡Hola, {self.nombre,' ',self.apellido,'residente en:',self.direccion}!")

personita=Persona("Alejandra",'Quiroz','los sauces 148 vista alegre') 
personita.saludar()

class Gato:
    
    def __init__(self, nombre,raza,color):
        self.nombre= nombre
        self.raza=raza
        self.color=color

    def miao(self):
        print(f"¡MIAO, {self.nombre,' ',self.raza,'prieto?:',self.color}!")
gatito=Gato("dark",'Siamés','negro')
gatito.miao()


class Producto:

    def __init__(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = float(precio)
        self.stock = int(stock)

    def orden(self):
        print(f"¡Merca: , {self.nombre, ' ',self.marca,' caro o pobre, el precio lo dirá u.u : ',self.precio,' cantidad: ',self.stock}!")

victoria= Producto("ale",'victoria secret', 20.5, 50)
victoria.orden()
    
        




