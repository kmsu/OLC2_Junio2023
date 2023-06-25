from ..Tabla_Simbolos.excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

class ToLowerCase(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.tipo = "any"
        super().__init__(nombre, parametros, instrucciones, fila, columna)

    def interpretar(self, arbol, tabla):
        simbolo = tabla.getTabla("toLower##Param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de toLowerCase", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        if(self.tipo=="string"):
            return simbolo.getValor().lower()
        return Excepcion("Semantico", "Se esperaba string en tolowercase", self.fila, self.columna)