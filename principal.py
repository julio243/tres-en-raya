#comienzo del juego
from ingresar import ingresar

c=0
print('*****TRES EN RAYA*****')
op=int(input('(1) comenzar partida | (0) salir: '))

if op == 1:
    ingresar(c)
elif op==0:
    print("GoodBye")          