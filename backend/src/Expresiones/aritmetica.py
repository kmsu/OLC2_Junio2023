from ..Abstract.abstract import Abstract
from ..Tabla_Simbolos.excepcion import Excepcion

class Aritmetica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq #
        self.op_der = op_der #
        self.op = op # *
        self.tipo = None
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table): 
            
        izq = self.op_izq.interpretar(tree, table)
        der = self.op_der.interpretar(tree, table)

        if self.op_izq.getTipo() != self.op_der.getTipo():
            return Excepcion("Semantico", "Error de tipos: el tipo " + str(self.op_izq.getTipo()) + " no coincide con tipo " + str(self.op_der.getTipo()) , self.fila, self.columna)

        if self.op == '+':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq + der
            elif self.op_izq.getTipo() == 'string':
                self.tipo = 'string'
                return izq + der
            else:
                return Excepcion("Semantico", "No es posible sumar " + str(self.op_izq.getTipo()) + " con " + str(self.op_der.getTipo()) , self.fila, self.columna)
            
        elif self.op == '-':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq - der
            else:
                return Excepcion("Semantico", "No es posible restar " + str(self.op_izq.getTipo()) + " con " + str(self.op_der.getTipo()) , self.fila, self.columna)
            
        elif self.op == '*':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq * der
            else:
                return Excepcion("Semantico", "No es posible multiplicar " + str(self.op_izq.getTipo()) + " con " + str(self.op_der.getTipo()) , self.fila, self.columna)
            
        elif self.op == '/':
            if self.op_izq.getTipo() == 'number':
                if der == 0:
                    return Excepcion("Semantico", "No es posible dividir entre 0", self.fila, self.columna)
                self.tipo = 'number'
                return izq / der
            else:
                return Excepcion("Semantico", "No es posible dividir " + str(self.op_izq.getTipo()) + " con " + str(self.op_der.getTipo()) , self.fila, self.columna)
            
        elif self.op == '%':
            if self.op_izq.getTipo() == 'number':
                if der == 0:
                    return 'Error: Modulo entre 0'
                self.tipo = 'number'
                return izq % der
            else:
                return Excepcion("Semantico", "No es posible obtener el modulo de " + str(self.op_izq.getTipo()) + " con " + str(self.op_der.getTipo()) , self.fila, self.columna)
            
        elif self.op == '^':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq ** der
            else:
                return Excepcion("Semantico", "No es posible obtener la potencia de " + str(self.op_izq.getTipo()) + " con " + str(self.op_der.getTipo()) , self.fila, self.columna)
            

    def getTipo(self):
        return self.tipo