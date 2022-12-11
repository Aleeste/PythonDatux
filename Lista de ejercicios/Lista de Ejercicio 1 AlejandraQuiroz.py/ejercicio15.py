#menu
def Hola():
    return "Hola"

def Suma(a, b):
    return a+b


while True:

    opcion=int(input("Saludar(1),Sumar(2),Finalizar"))
    
    if opcion==1: 
        Hola()
        print(Hola())
    elif  opcion==2:
        Suma(1,2)
        print(Suma(1,2))
    elif  opcion==3:
        break

   
    
