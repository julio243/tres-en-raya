#definicion final si es ganador o hay empate
import ingresar
def definicion(m):
    c=8

    if m[0][0] == m[1][1] == m[2][2] != ' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[2][0] == m[1][1] == m[0][2] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[0][0] == m[0][1] == m[0][2] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[1][0] == m[1][1] == m[1][2] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[2][0] == m[2][1] == m[2][2] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[0][0] == m[1][0] == m[2][0] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[0][1] == m[1][1] == m[2][1] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    elif m[0][2] == m[1][2] == m[2][2] !=' ':
        print('************************')
        print('*         WIN          *')
        print('************************')
    else:
        for i in range(3):
            for j in range(3):
                if m[i][j]==' ':
                    c-=1
                    break
                elif c==0:
                    print('************************')
                    print('*        EMPATE        *')
                    print('************************')
                    ingresar.ingresar(20)
                    break
