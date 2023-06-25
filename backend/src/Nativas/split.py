from ..Tabla_Simbolos.excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

class Split(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.tipo = "any"
        super().__init__(nombre, parametros, instrucciones, fila, columna)
#toFixed##Param1'},{'tipo':'any', 'id':'toFixed##Param2
    def interpretar(self, f, tabla):
        
        simbolo = tabla.getTabla("split##Param1")
        simbolo2 = tabla.getTabla("split##Param2")
        if simbolo == None: 
            #print(str("simbolo toupercase" + simbolo))
            return Excepcion("Semantico", "No se encontro el parametro de toFixed", self.fila, self.columna)
        if simbolo2 == None: 
            #print(str("simbolo toupercase" + simbolo))
            return Excepcion("Semantico", "No se encontro el valor toFixed", self.fila, self.columna)
        
        self.tipo = simbolo.getTipo()
        auxtipo = simbolo2.getTipo()
        
        if self.tipo == "string" and auxtipo == "string": 
           return simbolo.getValor().split(simbolo2.getValor())
        
        return Excepcion("Semantico", "Los tipos no son correctos")
       