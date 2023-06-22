from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion

class Arreglo(Abstract):
    
    def __init__(self, listaExpresiones, fila, columna):
        self.lsExp = listaExpresiones
        self.tipo = 'arreglo'
        self.lstExpresiones = []
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        arr = []
        #recorro la lista de expresiones para guardarlas en un arreglo
        for aux in self.lsExp:
            x = aux.interpretar(arbol, tabla)
            if isinstance(x, Excepcion):return x
            arr.append(x)
            self.lstExpresiones.append(aux)
            
        return arr

    def getTipo(self):
        return self.tipo

    def getlstExpresiones(self):
        return self.lstExpresiones
