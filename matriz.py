#creacion de la tabla del juego
def tabla():
    m=[]
    for i in range(3):
        m.append([])
        for j in range(3):
            m[i].append(' ')

    m[2][2]='x'
    print('   |     |   ')
    print(m[0][0],' | ',m[0][1],' | ',m[0][2])
    print('___|_____|___')
    print('   |     |   ')
    print(m[1][0],' | ',m[1][1],' | ',m[1][2])
    print('___|_____|___')
    print('   |     |   ')
    print(m[2][0],' | ',m[2][1],' | ',m[2][2])
    print('   |     |   ')

