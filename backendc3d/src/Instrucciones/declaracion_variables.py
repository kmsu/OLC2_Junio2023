from src.Expresiones.arreglo import Arreglo
from ..Tabla_Simbolos.excepcion import Excepcion
from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.simbolo import Simbolo
from ..Tabla_Simbolos.generador import Generador
from ..Abstract.return__ import Return

class Declaracion_Variables(Abstract):

    def __init__(self, ide, tipo, valor, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true      
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de valor de variable')
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Excepcion): return value # Analisis Semantico -> Error
        # Verificacion de tipos

        if self.tipo == None:
            self.tipo = self.valor.tipo

        if str(self.tipo) == str(self.valor.tipo):
            inHeap = self.valor.tipo == 'string' 
            simbolo = tabla.setTabla(self.ide, self.valor.tipo, inHeap , self.find)
        elif str(self.valor.tipo) == 'arreglo':
            i = 0
            recorrido = self.arreglo(self.valor.getlstExpresiones())
            for x in recorrido:
                if(x != self.tipo):
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
            generator.addComment('Error, tipo de dato diferente declarado.')
            result = Excepcion("Semantico", "se esperaba " + str(self.tipo) + " y se obtuvo " + str(self.valor.getTipo()) , self.fila, self.columna)
            return result

        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExpression(tempPos, 'P', simbolo.pos, '+')

        generator.setStack(tempPos, value)
        generator.addComment('Fin de compilacion de valor de variable')
        
    def setTipo(self, tipo):
        self.tipo = tipo

    def setValor(self, valor):
        self.valor = valor

    def arreglo(self, lista):
        #verificar  que la lista no este vacia 
        respuesta = []        
        i = 0
        for item in lista:
            #print("ITEM " + str(item))
            if isinstance(item, list) :
                aux = self.arreglo(item)
                #for x in aux:
                respuesta = respuesta + aux
            else:
                respuesta.append(item)
            i = i+1
        print("RESPUESTA: " + str(respuesta))
        return respuesta