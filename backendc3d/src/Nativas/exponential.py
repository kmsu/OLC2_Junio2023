from ..Tabla_Simbolos.excepcion import Excepcion
from ..Instrucciones.funcion import Funcion


class ToExponential(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.tipo = "any"
        super().__init__(nombre, parametros, instrucciones, fila, columna)

    def interpretar(self, f, tabla):
        simbolo = tabla.getTabla("toExponential##Param1")
        simbolo2 = tabla.getTabla("toExponential##Param2")
        if simbolo == None: 
            #print(str("simbolo toupercase" + simbolo))
            return Excepcion("Semantico", "No se encontro el parametro de toExponential", self.fila, self.columna)
        if simbolo2 == None: 
            #print(str("simbolo toupercase" + simbolo))
            return Excepcion("Semantico", "No se encontro el valor toExponential", self.fila, self.columna)
            
        self.tipo = simbolo.getTipo()
        auxtipo = simbolo2.getTipo()
        if self.tipo == "number" and auxtipo == "number": 
            #buscar punto
            posision_punto = 0
            letras = str(simbolo.getValor())
            for letra in letras:
                if(letra == "."):
                    break
                posision_punto += 1

            #siguiente posision 
            nuevaposp = posision_punto - simbolo2.getValor() + 1
            
            #correr punto
            i = 0
            res = ""
            for letra2 in letras:
                print(str(i) + "--" + str(nuevaposp))
                if(letra2 == "."):
                    continue
                elif(i==nuevaposp-1):
                    res += "."
                    res += letra2
                    print("poniendo punto en pos "+ str(nuevaposp))
                
                else:
                    res += letra2
                
                if(i == nuevaposp):
                    self.tipo = "string"
                    return "\"" + str(res)+ "+" + str(simbolo2.getValor())+"\""
                i+=1
            #respuesta
            print("respuesta " + str(res) )
            return float("{:.2f}".format(simbolo.getValor()))
        
        return Excepcion("Semantico", "Los tipos no son correctos")
       
