#Es vocal o no vocal#
UsuarioSolicite=input("Ingrese una letra: ")
if (len(UsuarioSolicite)>1) :
    print("No puede procesar el datos")
else: 
    if(UsuarioSolicite=='A' or UsuarioSolicite=='E' or UsuarioSolicite=='I' or UsuarioSolicite=='O' or UsuarioSolicite=='U'):
        print("Si es vocal")
    else:
        print('no es vocal')

