#comienzo del juego
from matriz import tabla
import ingresar

print('*****TRES EN RAYA*****')
op=int(input('(1) comenzar partida | (0) salir: '))

if op == 1:
    ingresar.ingresar()
elif op==0:
    print("GoodBye")          