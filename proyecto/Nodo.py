class Nodo:
    def __init__(self, tablero, movimiento, padre, heuristica) :
        self.tablero = tablero
        self.movimiento = movimiento
        self.heuristica = heuristica
        self.padre = padre
        self.hijos = []

    