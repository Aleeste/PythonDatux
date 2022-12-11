#.Realizar una función que tenga por parámetro un lista de números y aumente cada elemento en +1.#
cantidadElementos = int(input('cuantos elementos tendra la lista?'))
lista = []
for x in range (cantidadElementos):
    x = int(input('ingrese el elemento: '))
    x=x+1
    lista.append(x)

print('lista con valores aumentado +1:',lista)