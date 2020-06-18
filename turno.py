#comienzo del juego
from matriz import tabla
while True:
    print('TRES EN RAYA')
    op=int(input('(1) comenzar partida | (0) salir: '))
    if op == 1:
        print('el simbolo del primer jugador es "x"')
        print('elige la posicion')
        tabla()
    if op==0:
        print("GoodBye")    
        break
        