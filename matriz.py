#creacion de la tabla del juego
m=[]
def tabla(f,c):
    #creamos la tabla y ahi mismo lo llenamos.
    for i in range(3):
        m.append([])
        for j in range(3):
            m[i].append(' ')
    #los datos llegan de ingresar y se guardan y se imprimen
    m[f][c]='x'
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

