import math
from pprint import pprint
import numpy as np

from Nodo import Nodo

class Bot:
    def __init__( self, m_tableroG):
        self.m_tableroGanador = m_tableroG

    def have_won( self, tablero ):
        return np.array_equal(tablero, self.m_tableroGanador)

    def jugar( self, tablero ):
        pila_de_movimientos = []
        arbol = Nodo(tablero, None, None, None)

        while not self.have_won(arbol.tablero):
            self.extenderArbol(arbol,2)
            nodos4nivel = [ ]
            self.buscarHijos4nivel(arbol,nodos4nivel)
            min_heurstica = math.inf
            nodoEscogido = None
            for hijo in nodos4nivel:
                if hijo.heuristica < min_heurstica:
                    nodoEscogido = hijo
            arbol = nodoEscogido
         
        self.crearPilaDeMovimientos(nodoEscogido,pila_de_movimientos)
        
        pila_de_movimientos.reverse()
        
        return pila_de_movimientos

    def extenderArbol(self,nodoActual, nivel):
        movimientos = [ 'a', 'b', 'i', 'd' ]
       
        posicionCasillaVacia = np.where( np.array(nodoActual.tablero) == 0 )
        ( fila, columna ) = ( posicionCasillaVacia[ 0 ], posicionCasillaVacia[ 1 ] )
        
        if fila == 0:
            movimientos.remove('a')
        if fila == len( nodoActual.tablero ) - 1:
            movimientos.remove('b')
        if columna == 0:
            movimientos.remove('i')
        if columna == len( nodoActual.tablero ) - 1:
            movimientos.remove('d')
        
        if nivel == 4:
            for movimiento in movimientos:
                hijo = self.mover( movimiento, posicionCasillaVacia, np.copy(nodoActual.tablero) )
                if self.have_won(hijo):
                    return "gano"
                
                if not np.array_equal(nodoActual.padre.tablero, hijo ):
    
                    nodoArbol = Nodo(hijo,movimiento,nodoActual,self.heuristica(hijo))
                    nodoActual.hijos.append(nodoArbol)
                
            
        else:
            for movimiento in movimientos:
                hijo = self.mover( movimiento, posicionCasillaVacia, np.copy(nodoActual.tablero) )
                if self.have_won(hijo):
                    return "gano"

                if not nodoActual.padre is None:
                    if not np.array_equal(nodoActual.padre.tablero, hijo ):
                        nodoArbol = Nodo(hijo,movimiento,nodoActual,None)
                        nodoActual.hijos.append(nodoArbol)
                        self.extenderArbol(nodoArbol,nivel + 1)
                else:
                    if not np.array_equal(nodoActual.tablero, hijo ):
                        nodoArbol = Nodo(hijo,movimiento,nodoActual,None)
                        nodoActual.hijos.append(nodoArbol)
                        self.extenderArbol(nodoArbol,nivel + 1)
            
    def buscarHijos4nivel(self, nodoActual,nodos4nivel):
        if len(nodoActual.hijos) == 0:
            nodos4nivel.append(nodoActual)
        else:
            for hijo in nodoActual.hijos:
                self.buscarHijos4nivel(hijo,nodos4nivel)

    def crearPilaDeMovimientos(self,nodoEscogido, pila_de_movimientos):
        if not nodoEscogido.movimiento is None:
            pila_de_movimientos.append(nodoEscogido.movimiento)
            self.crearPilaDeMovimientos(nodoEscogido.padre, pila_de_movimientos)


    def moveDerecha(self, fila, columna, tablero):
        tablero[fila][columna], tablero[fila][columna + 1] = tablero[fila][columna + 1], tablero[fila][columna]
    
    def moveAbajo(self,fila,columna, tablero):
        tablero[fila][columna], tablero[fila + 1][columna] = tablero[fila + 1][columna], tablero[fila][columna]
        
    def moveIzquierda(self,fila,columna, tablero):
        tablero[fila][columna], tablero[fila][columna - 1] = tablero[fila][columna - 1], tablero[fila][columna]

    def moveArriba(self, fila, columna, tablero):
        tablero[fila][columna], tablero[fila - 1][columna] = tablero[fila - 1][columna], tablero[fila][columna]

    def mover(self, movimiento, casillaVacia, tablero ):
        if movimiento == 'a':
            self.moveArriba( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        elif movimiento == 'b':
            self.moveAbajo( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        elif movimiento == 'i':
            self.moveIzquierda( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        elif movimiento == 'd':
            self.moveDerecha( int( casillaVacia[0] ), int( casillaVacia[1] ), tablero )
        return tablero

    def heuristica(self, hijo):
        H = 0
        tablero = np.array(hijo)
        tableroG = np.array( self.m_tableroGanador )

        for i in range(1, len( self.m_tableroGanador ) * len( self.m_tableroGanador )):
            posTablero = np.where(tablero == i)
            posTableroG = np.where(tableroG == i)

            distFila = abs( int(posTableroG[0]) - int(posTablero[0])) 
            disColumna = abs( int(posTableroG[1]) - int(posTablero[1]))
            
            H += distFila + disColumna

        return H