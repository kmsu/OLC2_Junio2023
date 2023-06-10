from ..Abstract.abstract import Abstract

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
            return 'Error de tipos'

        if self.op == '+':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq + der
            elif self.op_izq.getTipo() == 'string':
                self.tipo = 'string'
                return izq + der
            else:
                return "Error no se pueden sumar los tipos encontrados en fila: " + str(self.fila) + " columna: " + str(self.columna)
            
        elif self.op == '-':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq - der
            else:
                return "Error no se pueden restar los tipos encontrados en fila: " + str(self.fila) + " columna: " + str(self.columna)
            
        elif self.op == '*':
            if self.op_izq.getTipo() == 'number':
                self.tipo = 'number'
                return izq * der
            else:
                return "Error no se pueden multiplicar los tipos encontrados en fila: " + str(self.fila) + " columna: " + str(self.columna)
            
        elif self.op == '/':
            if self.op_izq.getTipo() == 'number':
                if der == 0:
                    return 'Error: Division entre 0'
                return izq / der
            else:
                return "Error no se pueden dividir los tipos encontrados en fila: " + str(self.fila) + " columna: " + str(self.columna)
            
        elif self.op == '%':
            if self.op_izq.getTipo() == 'number':
                if der == 0:
                    return 'Error: Modulo entre 0'
                return izq % der
            else:
                return "Error no se puede obtener el modulo con los tipos encontrados en fila: " + str(self.fila) + " columna: " + str(self.columna)
            
        elif self.op == '^':
            if self.op_izq.getTipo() == 'number':
                return izq ** der
            else:
                return "Error no se puede obtener la potencia con los tipos encontrados en fila: " + str(self.fila) + " columna: " + str(self.columna)
            

    def getTipo(self):
        return self.tipo