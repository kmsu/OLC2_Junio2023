from ..Tabla_Simbolos.excepcion import Excepcion
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.simbolo import Simbolo

class Asignacion(Abstract):

    def __init__(self, ide, valor, fila, columna):
        self.ide = ide # a
        self.valor = valor # 4, 'hola', true
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Excepcion): return value # Analisis Semantico -> Error

        variable = tabla.getTabla(self.ide)
        tipoVariable = variable.getTipo()
        # Verificacion de tipos
        if tipoVariable == None:
            tipoVariable = self.valor.tipo

        if str(tipoVariable) == str(self.valor.tipo):
            simbolo = Simbolo(str(self.ide), self.valor.tipo, value, None, self.fila, self.columna)
            result = tabla.updateTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None
        else:
            result = Excepcion("Semantico", "se esperaba " + str(self.tipo) + " y se obtuvo " + str(self.valor.getTipo()) , self.fila, self.columna)
            return result
        
    def setTipo(self, tipo):
        self.tipo = tipo

    def setValor(self, valor):
        self.valor = valor