from ..Tabla_Simbolos.simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion
from ..Tabla_Simbolos.tabla_simbolos import TablaSimbolos
from src.Expresiones.primitivos import Primitivos
from src.Instrucciones.declaracion_variables import Declaracion_Variables

class CWhile(Abstract):

    def __init__(self, expresion, bloqueWhile, fila, columna):
        self.expresion = expresion
        self.bloqueWhile = bloqueWhile
        self.fila = fila
        self.columna = columna
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        print(str(self.bloqueWhile) + "este es el bloque")
        # a expresion se le asigna un valor (1 , "2" , true)
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO
        expresion = self.expresion.interpretar(arbol, tabla)
        # si la expresion viene mal, salta excpcion
        if isinstance(expresion, Excepcion): return expresion
        # obtenemos el tipo de la expresion
        tipo = self.expresion.getTipo()
        # vemos que sea booleano
        if tipo == 'boolean':

            # Recorriendo las instrucciones
            #expresion va a ser igual a un interpretar del bloque while -- buscamos en nueva tabla su valor
            while (expresion):
                # nuevo_valor = expresion[i]               
                # simbolo = Simbolo(self.variable.ide, self.variable.tipo, nuevo_valor, self.fila, self.columna)
                # # Actualizando el valor de la variable en la tabla de simbolos
                # valor = nuevaTabla.updateTabla(simbolo)
                # if isinstance(valor, Excepcion): return valor 
                
                for instruccion in self.bloqueWhile:
                    result = instruccion.interpretar(arbol, nuevaTabla)
                    if isinstance(result, Excepcion):
                        arbol.excepciones.append(result)
                
                expresion = self.expresion.interpretar(arbol, nuevaTabla)
                
                # simbolo = Simbolo(str(self.ide), self.valor.tipo, expresion, self.fila, self.columna)
                # result = tabla.setTabla(simbolo)
                # if isinstance(result, Excepcion): return result
                #gettable (expresion) - esto nos devolvera la fila de la tabla y sacamos valor
                #expresion = False
                
            return None
            



