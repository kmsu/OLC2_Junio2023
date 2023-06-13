from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion

class Imprimir(Abstract):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion # <<Class.Primitivos>>
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        value = ""
        for aux in self.expresion:
            x = aux.interpretar(tree, table)
            if isinstance(x, Excepcion):
                value = x.toString()
            else: 
                value += str(aux.interpretar(tree, table))
        #print(value)
        tree.updateConsola(str(value))
        return value