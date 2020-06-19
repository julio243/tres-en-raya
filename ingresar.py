#ingresamos en que posision se van a ir cada signo
from matriz import tabla
def ingresar(c):
        
    while c<12:       #ponemos un while hasta que no queden movimientos
        #if para si es par le toca jugar a player1 si es impar al player2
        if c%2==0:
            print('PLAYER 1')
            fila=int(input("ingresa el numero de la fila: "))
            columna=int(input("ingresa el numero de la columna: "))
            
        else:
            print('PLAYER 2')
            fila=int(input("ingresa el numero de la fila: "))
            columna=int(input("ingresa el numero de la columna: "))
             
        
        #se manda los datos a matriz
        tabla(fila,columna,c)
        c+=1
        