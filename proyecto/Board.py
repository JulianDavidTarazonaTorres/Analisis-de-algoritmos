import random
import numpy as np
class Board:

    #Atributos
    tam = None
    m_tablero = None
    m_tableroG = None


    def __init__( self, tam):
        self.tam = tam
        self.m_tablero = [ [j+i*tam + 1 for j in range(tam)] for i in range(tam) ]
        self.m_tableroG = [ [j+i*tam + 1 for j in range(tam)] for i in range(tam) ]

        self.m_tablero[tam -1][tam-1] = 0
        self.m_tableroG[tam -1][tam-1] = 0
        for i in range(tam):
            random.shuffle(self.m_tablero[ i ])
        random.shuffle(self.m_tablero)

    def __str__(self):
        s = ""  
        for k in range( len( self.m_tablero ) ):
            s += "+-----"
        s += "+\n"
        for i in range(len( self.m_tablero )):
            for k in range( len( self.m_tablero ) ):
                s += "|     "
            s += "|\n"
            for k in range( len( self.m_tablero ) ):
                if self.m_tablero[i][k] == 0:
                    s += "|  " + " " + "  "
                else:
                    if self.m_tablero[i][k] < 10:
                        s += "|  " + str(self.m_tablero[i][k]) + "  "
                    else:
                        s += "| " + str(self.m_tablero[i][k]) + "  "
            s += "|\n"
            for k in range( len( self.m_tablero ) ):
                s += "|     "
            s += "|\n"
            for k in range( len( self.m_tablero ) ):
                s += "+-----"
            s += "+\n"
        
        return s
    
    def have_won( self ):
        return np.array_equal(self.m_tablero, self.m_tableroG)
    
    def moves( self, movimiento):

        posicionCasillaVacia = np.where( np.array(self.m_tablero) == 0 )
        ( fila, columna ) = ( posicionCasillaVacia[ 0 ], posicionCasillaVacia[1] )

        movimientosPosibles = [ 'a', 'b', 'i', 'd']

        if fila == 0:
            movimientosPosibles.remove('a')
        if fila == self.tam - 1:
            movimientosPosibles.remove('b')
        if columna == 0:
            movimientosPosibles.remove('i')
        if columna == self.tam - 1:
            movimientosPosibles.remove('d')

        if movimiento in movimientosPosibles:
            if movimiento == "i":
                self.moveIzquierda( int(fila),int(columna) )
            elif movimiento == "a":
                self.moveArriba( int(fila),int(columna) )
            elif movimiento == "b":
                self.moveAbajo( int(fila),int(columna) )
            elif movimiento == "d":
                self.moveDerecha( int(fila),int(columna) )
            return True
        else:
            return False

    def moveDerecha(self,fila,columna):
        print("mover derecha")
        self.m_tablero[fila][columna], self.m_tablero[fila][columna + 1] = self.m_tablero[fila][columna + 1], self.m_tablero[fila][columna]
    
    def moveAbajo(self,fila,columna):
        print("mover abajo")
        self.m_tablero[fila][columna], self.m_tablero[fila + 1][columna] = self.m_tablero[fila + 1][columna], self.m_tablero[fila][columna]
        
    def moveIzquierda(self,fila,columna):
        print("mover izquierda")
        self.m_tablero[fila][columna], self.m_tablero[fila][columna - 1] = self.m_tablero[fila][columna - 1], self.m_tablero[fila][columna]

    def moveArriba(self,fila,columna):
        print("mover Arriba")
        self.m_tablero[fila][columna], self.m_tablero[fila - 1][columna] = self.m_tablero[fila - 1][columna], self.m_tablero[fila][columna]
                        