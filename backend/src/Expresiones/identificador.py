from ..Tabla_Simbolos.excepcion import Excepcion
from ..Abstract.abstract import Abstract

class Identificador(Abstract):
    def __init__(self, ide, fila, columna, tipo = None):
        self.ide = ide
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.sym = None

    def interpretar(self, arbol , tabla):
        simbolo = tabla.getTabla(self.ide)
        if simbolo == None:
            return Excepcion("Semantico", "Variable no encontrada class identificador " + self.ide, self.fila, self.columna)
        self.tipo = simbolo.getTipo()
        self.sym = simbolo
        return simbolo.getValor()

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide
    
    def getArregloTipo(self):
        return self.sym.getValorArreglo()