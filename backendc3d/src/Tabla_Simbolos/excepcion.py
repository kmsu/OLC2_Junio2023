class Excepcion:

    def __init__(self, tipo, desc, fila, columna):
        self.tipo = tipo
        self.desc = desc
        self.fila = fila
        self.columna = columna
    
    def toString(self):
        return self.tipo + ' - ' + self.desc + ' [' + str(self.fila) + ', ' + str(self.columna) + '];'
    
    def toString2(self):
        respuesta = []

        respuesta.append(self.tipo)
        respuesta.append(self.desc)
        respuesta.append(self.fila)
        respuesta.append(self.columna)

        return respuesta