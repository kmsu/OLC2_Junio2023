from ..Tabla_Simbolos.excepcion import Excepcion
from ..Abstract.abstract import Abstract

class Relacional_Logica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq #
        self.op_der = op_der #
        self.op = op # *
        self.tipo = 'boolean'
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        izq = self.op_izq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq #valido la instancia por si es identificador de variable

        if self.op != '!': #Este if es porque si el operador es ! no existira el op_der
            der = self.op_der.interpretar(tree, table)
            if isinstance(der, Excepcion): return der
            if self.op_izq.getTipo() != self.op_der.getTipo():
                auxIzq = str(self.op_izq.getTipo())
                auxDer = str(self.op_der.getTipo())
                return Excepcion("Semantico", "Error de tipos: el tipo " + auxIzq + " no coincide con tipo " + auxDer , self.fila, self.columna)

        if self.op == '<':
            return izq < der
        elif self.op == '>':
            return izq > der
        elif self.op == '===':
            return izq == der
        elif self.op == '!==':
            return izq != der
        elif self.op == '<=':
            return izq <= der
        elif self.op == '>=':
            return izq >= der
        elif self.op == '!':
            return not izq
        elif self.op == '&&':
            return izq and der
        elif self.op == '||':
            return izq or der
        else:
            return Excepcion("Semantico", "Operacion no valida.", self.fila, self.columna)

    def getTipo(self):
        return self.tipo
    
    def getValor(self, tipo, val):
        # aqui hacen validacion del tipo de dato
        return str(val)