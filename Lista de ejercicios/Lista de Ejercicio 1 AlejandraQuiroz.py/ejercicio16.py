listaedades=[12,32,323,12,12,3,4,21]
Nombre=(input("Ingrese su nombre"))
edad=int(input("Ingrese su edad"))

for edad in listaedades:
    if(edad>=18):
      print("Es mayor de edad:" + str(edad))
    else:
        print("Es menor de edad:"+ str(edad))



