listaEstudiantes =int(input("ingrese una lista de un estudiante: "))
lista = []
for i in range(listaEstudiantes):
    elemento = (input("Ingrese elemento :"))
    lista.append(elemento)

print(lista)

print('ultimo elemento; ',lista[-1])    

print('Lista invertida: ')
lista.reverse()
print(lista)