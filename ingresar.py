from matriz import tabla
def ingresar():
    c=0
    while c<9:
        if c%2==0:
            print('PLAYER 1')
            fila=int(input("ingresa el numero de la fila: "))
            columna=int(input("ingresa el numero de la columna: "))
            tabla(fila,columna)
            c+=1

        else:
            print('PLAYER 2')
            fila=int(input("ingresa el numero de la fila: "))
            columna=int(input("ingresa el numero de la columna: "))
            tabla(fila,columna)
            c+=1 
    