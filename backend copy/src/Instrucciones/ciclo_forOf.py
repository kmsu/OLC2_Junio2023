from ..Tabla_Simbolos.simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion
from ..Tabla_Simbolos.tabla_simbolos import TablaSimbolos
from src.Expresiones.primitivos import Primitivos
from src.Instrucciones.declaracion_variables import Declaracion_Variables

class ForOf(Abstract):

    def __init__(self, variable, expresion, bloqueFor, fila, columna):
        self.variable = variable
        self.expresion = expresion
        self.bloqueFor = bloqueFor
        self.fila = fila
        self.columna = columna
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO

        expresion = self.expresion.interpretar(arbol, nuevaTabla)
        if isinstance(expresion, Excepcion): return expresion

        tipo = self.expresion.getTipo()
        self.variable.setTipo(tipo)
        
        if tipo == 'string':
            inicio =  Primitivos('string', expresion[0], 0, 0)
            self.variable.setValor(inicio)
            id = self.variable.interpretar(arbol, nuevaTabla)
            if isinstance(id, Excepcion): return id

            # Recorriendo las instrucciones
            i = 0
            while i<len(expresion):
                nuevo_valor = expresion[i]               
                simbolo = Simbolo(self.variable.ide, self.variable.tipo, nuevo_valor, None, self.fila, self.columna)
                # Actualizando el valor de la variable en la tabla de simbolos
                valor = nuevaTabla.updateTabla(simbolo)
                if isinstance(valor, Excepcion): return valor
                
                for instruccion in self.bloqueFor:
                    result = instruccion.interpretar(arbol, nuevaTabla)
                    if isinstance(result, Excepcion):
                        arbol.excepciones.append(result)
                
                i = i+1
                
            return None
            



