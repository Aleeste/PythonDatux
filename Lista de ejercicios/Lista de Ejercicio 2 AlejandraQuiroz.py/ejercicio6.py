def saludar(nombre):
    return "hola"+nombre
print(saludar("Alejandra"))

def realizarTarea(tarea):
    return "hola"+tarea
print(realizarTarea("matematica"))
    
def despedirse(nombre):
    return "hola"+nombre
print(despedirse("Chao"))

N1=int(input("Ingrese el primer numero"))
N2=int(input("Ingrese el segundo numero"))
if(N1>N2 ):
    print("Si es mayor"+str(N1))
else : 
    print("No es menor"+str(N2))