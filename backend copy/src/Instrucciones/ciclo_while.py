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
        # a expresion se le asigna un valor (1 , "2" , true)
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO
        expresion = self.expresion.interpretar(arbol, nuevaTabla)
        # si la expresion viene mal, salta excpcion
        if isinstance(expresion, Excepcion): return expresion
        # obtenemos el tipo de la expresion
        tipo = self.expresion.getTipo()
        # vemos que sea booleano
        if tipo == 'boolean':

            # Recorriendo las instrucciones
            #expresion va a ser igual a un interpretar del bloque while -- buscamos en nueva tabla su valor
            while (expresion):                
                for instruccion in self.bloqueWhile:
                    result = instruccion.interpretar(arbol, nuevaTabla)
                    if isinstance(result, Excepcion):
                        arbol.excepciones.append(result)
                
                expresion = self.expresion.interpretar(arbol, nuevaTabla)
                
            return None
            



