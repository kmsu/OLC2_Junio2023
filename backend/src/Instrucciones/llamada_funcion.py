from ..Tabla_Simbolos.simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion
from ..Tabla_Simbolos.tabla_simbolos import TablaSimbolos

class Llamada_Funcion(Abstract):

    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        #self.tipo = None
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        result = arbol.getFuncion(self.nombre)
        if result == None:
            return Excepcion("Semantico", "No se encontro la funcion: " + str(self.nombre), str(self.fila), str(self.columna))
        entorno = TablaSimbolos(arbol.getTsglobal())
        
        #print("esto viene en parametros: "+str(self.parametros))
        if(self.parametros != None):
            #Comprobamos la cantidad de parametros de la llamada de la funcion y de la funcion (deben coincidir)
            if len(self.parametros) == len(result.parametros):
                contador = 0
                for expresion in self.parametros:
                    resultE = expresion.interpretar(arbol, tabla)
                    if isinstance(resultE, Excepcion): return resultE
                    if result.parametros[contador]['tipo'] == expresion.tipo:
                        simbolo = Simbolo(str(result.parametros[contador]['id']), expresion.tipo, resultE, None, self.fila, self.columna)
                        resultT = entorno.setTablaFuncion(simbolo)
                    elif result.parametros[contador]['tipo'] == 'any':
                        simbolo = Simbolo(str(result.parametros[contador]["id"]), expresion.tipo, resultE,None, self.fila, self.columna)
                        resultT = entorno.setTablaFuncion(simbolo)
                    else:
                        return Excepcion("Semantico", "Tipo de dato diferente en Parametros", str(self.fila), str(self.columna))
                    contador += 1

        value = result.interpretar(arbol, entorno) # me puede retornar un valor

        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo
        return value
    
    def getTipo(self):
        return self.tipo