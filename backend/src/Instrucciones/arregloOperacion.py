from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion
from ..Tabla_Simbolos.simbolo import Simbolo

class ArregloOperacion(Abstract):

    def __init__(self, id, lstIndice, valor, fila, columna):
        self.id = id
        self.lstIndice = lstIndice
        self.valor = valor
        self.tipo = None
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        #asignacion
        if(self.valor != None):
            #traemos el simbolo (variable) que contiene el arreglo
            simbolo = tabla.getTabla(self.id)

            #expresion que se va a guardar en el arreglo
            val = self.valor.interpretar(arbol, tabla)
            if isinstance(val, Excepcion): return val
            tipoval = self.valor.getTipo()
            
            tmp = simbolo.getValor() 
            tmp2 = simbolo.getValor() 
            pos = 0
            i = 0
            while i<len(self.lstIndice):
                pos = self.lstIndice[i].interpretar(arbol, tabla)
                if isinstance(pos, Excepcion): return pos
                if(self.lstIndice[i].getTipo() == 'number'):
                    pos = int(pos)
                    #aqui tendríamos que devolver una excepcion si fuera un decimal
                    if(i<len(self.lstIndice) -1 ):tmp = tmp[pos]
                i = i + 1
            
            tmp[pos] = val
            nuevoSimbolo = Simbolo(str(self.id), 'arreglo', tmp2, None, self.fila, self.columna)
            result = tabla.updateTabla(nuevoSimbolo)
            if isinstance(result, Excepcion): return result
        
        else:
            #getValor
            #traemos el simbolo (variable) que contiene el arreglo
            simbolo = tabla.getTabla(self.id)
            
            tmp = simbolo.getValor()
            tmp2 = simbolo.getValorArreglo()
            pos = 0
            i = 0
            while i<len(self.lstIndice):
                pos = self.lstIndice[i].interpretar(arbol, tabla)
                if isinstance(pos, Excepcion): return pos
                if(self.lstIndice[i].getTipo() == 'number'):
                    pos = int(pos)
                    #aqui tendríamos que devolver una excepcion si fuera un decimal
                    # if(i<len(self.lstIndice) -1 ):
                    #     tmp = tmp[pos]
                    #     tmp2 = tmp2[pos]
                    #     print("este es tmp en el if de indices en arreglo op " + str(tmp))
                        
                i = i + 1
                tmp = tmp[pos]
                print("TMP1 " + str(tmp)) 
                tmp2 = tmp2[pos]
                print("TMP2 " + str(tmp2)) 
                #tmp2 = tmp2[pos]
                #self.tipo = tmp2[pos]
            self.tipo = tmp2
            

            print("esto viene en self tipo " + str(self.tipo))

            return tmp #no deberia retornar el numero, sino una expresion 
                
        
        return None
            
    def getTipo(self):
        return self.tipo
    