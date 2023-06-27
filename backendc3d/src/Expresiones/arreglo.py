from src.Expresiones.identificador import Identificador
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion

class Arreglo(Abstract):
    
    def __init__(self, listaExpresiones, fila, columna):
        self.lsExp = listaExpresiones
        self.tipo = 'arreglo'
        self.valores = []
        self.lstTipos = []
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        
        #recorro la lista de expresiones para guardarlas en un arreglo
        for aux in self.lsExp:
            x = aux.interpretar(arbol, tabla)
            if isinstance(x, Excepcion):return x
            self.valores.append(x)            
            if(aux.getTipo() == 'arreglo'):
                if isinstance(aux, Identificador):
                    self.lstTipos.append(aux.getArregloTipo())
                else:    
                    self.lstTipos.append(aux.getlstExpresiones())
            else:
                self.lstTipos.append(aux.getTipo())
                        
        return self.valores

    def getTipo(self):
        return self.tipo

    def getlstExpresiones(self):
        return self.lstTipos
    
    def getValor(self):
        return self.valores
