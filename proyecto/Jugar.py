import sys
from Board import *
from Bot import Bot

if len( sys.argv ) < 2:
    print( "Usage: python3", sys.argv[ 0 ], "size" )
    sys.exit( 1 )

# end if
tam = int( sys.argv[ 1 ] )

board = Board( tam )

#movimientos: numero,direccion. ejemplo 8,a
#a = arriba
#d = derecha
#i = izquierda
#b = abajo

bot = Bot( board.m_tableroG )

print("\nMovimientos:\na = arriba \nd = derecha \ni = izquierda \nb = abajo")
print( board )

for movimiento in bot.jugar( board.m_tablero ):
    board.moves( movimiento )

print( board )
print('You Won!')

