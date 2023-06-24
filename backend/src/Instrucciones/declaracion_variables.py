from ..Tabla_Simbolos.excepcion import Excepcion
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.simbolo import Simbolo

class Declaracion_Variables(Abstract):

    def __init__(self, ide, tipo, valor, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Excepcion): return value # Analisis Semantico -> Error
        # Verificacion de tipos

        #print("tipo de arrelgo en declaracion: " + str(self.valor.tipo))
        if self.tipo == None:
            self.tipo = self.valor.tipo

        if str(self.tipo) == str(self.valor.tipo):
            if(self.valor.tipo == 'arreglo'):
                #print("Arreglo de tipos desde declaracion " + str(self.valor.getlstExpresiones()))
                simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.valor.getlstExpresiones(), self.fila, self.columna)
            else:
                simbolo = Simbolo(str(self.ide), self.valor.tipo, value, None, self.fila, self.columna)
            result = tabla.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None
        elif str(self.valor.tipo) == 'arreglo':
            i = 0
            print(str(self.valor.getlstExpresiones()) + " lista tipos")
            for x in self.valor.getlstExpresiones():
                if(x != self.tipo):
                    print("tipo de los elementos no coincide con el tipo del arreglo")
                    respuesta = [] 
                    simbolo = Simbolo(str(self.ide), self.valor.tipo, respuesta, respuesta, self.fila, self.columna)
                    result = tabla.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    return None
                
                i = i + 1
            simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.valor.getlstExpresiones(), self.fila, self.columna)
            result = tabla.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None

        else:
            result = Excepcion("Semantico", "se esperaba " + str(self.tipo) + " y se obtuvo " + str(self.valor.getTipo()) , self.fila, self.columna)
            return result
        
    def setTipo(self, tipo):
        self.tipo = tipo

    def setValor(self, valor):
        self.valor = valor