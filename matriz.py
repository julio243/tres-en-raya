#creacion de la tabla del juego
import ingresar,definirfinal
m=[]
def tabla(f,c,cont):
    
    #creamos la tabla vacia
    for i in range(3):
        m.append([])
        for j in range(3):
            m[i].append(' ')
    
    #se mira si el sitio esta ocupado, si no lo esta ingresa el signo dependiendo del player
    if m[f][c]==' ':
        if cont%2==0:
            m[f][c]='x'
        else:
            m[f][c]='o'
    else:
        print('sitio ocupado')
        cont=-1
        ingresar.ingresar(cont)        
    
    #imprimir la tabla
    print('   |     |   ')
    print(m[0][0],' | ',m[0][1],' | ',m[0][2])
    print('___|_____|___')
    print('   |     |   ')
    print(m[1][0],' | ',m[1][1],' | ',m[1][2])
    print('___|_____|___')
    print('   |     |   ')
    print(m[2][0],' | ',m[2][1],' | ',m[2][2])
    print('   |     |   ')
    
    definirfinal.definicion(m)
