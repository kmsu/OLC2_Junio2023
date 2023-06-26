import json
from ..Tabla_Simbolos.excepcion import Excepcion

class TablaSimbolos:

    def __init__(self, anterior = None):
        self.tabla = {} # Al inicio la tabla esta vacia
        self.anterior = anterior # Apuntador al entorno anterior
    
    def getTablaG(self):
        return self.tabla
    
    def setTabla(self, simbolo):
        # Aqui va la verificacion de que no se declare una variable dos veces
        self.tabla[simbolo.getID()] = simbolo
        print("se declaro variable " + str(simbolo.getID()))
    
    def setTablaFuncion(self, simbolo):
        self.tabla[simbolo.getID()] = simbolo
    
    def getTabla(self, ide): # Aqui manejamos los entornos :3
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla: #estructura python: busca ide en la lista tabla
                return tablaActual.tabla[ide]
            else:
                tablaActual = tablaActual.anterior
        return None
    
    def updateTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.getID() in tablaActual.tabla:
                tablaActual.tabla[simbolo.getID()].setValor(simbolo.getValor())
                return None
                # Si necesitan cambiar el tipo de dato
                # tablaActual.tabla[simbolo.getID()].setTipo(simbolo.getTipo())
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada. " + str(simbolo.getID()), simbolo.getFila(), simbolo.getColumna())

    def reporteTS(self):
        list = []
        cont = 1
        entorno = "Global"
        tablaActual = self
        while tablaActual != None:
            for ide in tablaActual.tabla: #estructura python: busca ide en la lista tabla
                temp = tablaActual.tabla[ide]
                var = json.dumps('{"no":'+cont+', "id": "' + temp.getId()+ '", "TipoDato": "'+ temp.getTipo() + '", "valor": "'+ str(temp.getValor()) + '", "entorno": "'+ entorno + '", "linea": '+ temp.getFila()+', "columna": ' + temp.getColumna()+' }')
                #return tablaActual.tabla[ide]
                list.append(var)
            entorno = "Local"
            tablaActual = tablaActual.anterior
        return list

