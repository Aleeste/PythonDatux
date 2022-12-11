#Menu#
N1=int(input("Ingrese el primer numero"))
N2=int(input("Ingrese el segundo numero"))
IngreseMenu=int(input("Suma(1),resta(2),multiplicacion(3)"))
if(IngreseMenu==1):
    print(N1+N2)
elif(IngreseMenu==2):
    print(N1-N2)
elif(IngreseMenu==3):
    print(N1*N2)
else:
    print("Operacion no valida")

