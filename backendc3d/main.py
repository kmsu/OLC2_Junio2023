# CORS -> Cross Origin Resource Sharing
# Si no existe el CORS, no se puede acceder a los recursos de un servidor desde otro servidor
from typing import Dict, List
from src.Nativas.concat import Concat
from src.Nativas.split import Split
from src.Nativas.exponential import ToExponential
from src.Nativas.tofixed import ToFixed
from src.Nativas.tostring import String
from src.Nativas.tolowercase import ToLowerCase
from src.Nativas.touppercase import ToUpperCase
from src.Nativas.typeof import Typeof
from Analizador_Sintactico import parse as Analizar
from src.Instrucciones.funcion import Funcion
from src.Expresiones.identificador import Identificador
from src.Instrucciones.llamada_funcion import Llamada_Funcion
from src.Instrucciones.imprimir import Imprimir
from src.Tabla_Simbolos.Tipo import TIPO
from src.Tabla_Simbolos.arbol import Arbol
from src.Tabla_Simbolos.excepcion import Excepcion
from src.Tabla_Simbolos.tabla_simbolos import TablaSimbolos
from src.Instrucciones.declaracion_variables import Declaracion_Variables
from src.Tabla_Simbolos.simbolo import Simbolo
from Analizador_Lexico import errores, tokens, lexer
from flask import Flask, request
import json
from flask_cors import CORS
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)
CORS(app)


@app.route('/saludo', methods = ["GET"])
def saludo():
    return {"mensaje": "Hola mundo!"}


@app.route('/compilar', methods = ["POST","GET"])
def compilar():
    if request.method == "POST":
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        #print(entrada)
        global tmp_val
        tmp_val = entrada["codigo"]
        #print(tmp_val)
        return redirect(url_for("salida"))
    else:
        return {"mensaje": "No compilado"}


@app.route('/salida')
def salida():
    global tmp_val
    global Excepciones 
    #print(tmp_val)
    global Tabla
    Tabla = {}
    instrucciones = Analizar(tmp_val)
    ast = Arbol(instrucciones)
    agregarNativas(ast)
    TsgGlobal = TablaSimbolos()
    ast.setTsglobal(TsgGlobal)
    

    for error in errores:
        ast.setExcepciones(error)

    # for instruccion in ast.getInstr():
    #     value = instruccion.interpretar(ast, TsgGlobal)
    #     if isinstance(value, Excepcion):
    #         ast.setExcepciones(value)
    #print(str(ast.getInstr()) + " esta es la Instruccion")

    
    for instruccion in ast.getInstr():
        
        #value = instruccion.interpretar(ast, TsgGlobal)
        if isinstance(instruccion, Funcion):
            ast.setFunciones(instruccion )
        
    
    for instruccion in ast.getInstr():
        if not(isinstance(instruccion, Funcion)):
            value = instruccion.interpretar(ast, TsgGlobal)
            if isinstance(value, Excepcion):
                ast.setExcepciones(value)

    Excepciones = ast.getExcepciones()
    global Simbolos
    Simbolos = ast.getTsglobal().getTablaG()
    
    consola = str(ast.getConsola())
    print('Consola: ', consola)
    if ast.excepciones != None:
        for aux in ast.excepciones:
            print('Errores', aux.toString())
    return json.dumps({'consola':consola, 'mensaje': 'Compilado :3'})

@app.route('/getErrores')
def getErrores():
    global Excepciones
    aux = []
    for x in Excepciones:
        aux.append(x.toString2())
    json_data= []
    i = 0
    for di in aux:
        data = {'Tipo':di[0] , 'Linea':di[2],'Columna':di[2],'Descripcion':di[1]} 
        json_data.append(data)
        
    return {"valores":json_data}

@app.route('/getTS')
def getTabla():
    global Simbolos
    Dic = []
    for x in Simbolos:
        aux = Simbolos[x].getValor()
        tipo = Simbolos[x].getTipo()
        #tipo = getTipo(tipo)
        fila = Simbolos[x].getFila()
        colum = Simbolos[x].getColumna()
       
        if isinstance(aux, List):
            a = []
            b = []
            a.append(str(x))
            if(len(aux)>0):
                aux = getValores(aux)
                a.append(str(aux))
            else:
                a.append(b)
            
            a.append('Array')
            a.append('Global')
            a.append(str(fila))
            a.append(str(colum))
            Dic.append(a)
        elif isinstance(aux, Dict):
            aux = getValores2(aux)
            a = []
            a.append(str(x))
            a.append(str(aux))
            a.append('Struct')
            a.append('Global')
            a.append(str(fila))
            a.append(str(colum))
            Dic.append(a)
        else:
            a = []
            a.append(str(x))
            a.append(tipo)
            a.append(str(aux))
            a.append('Global')
            a.append(str(fila))
            a.append(str(colum))
            Dic.append(a)
    json_data= []
    i = 1
    for di in Dic:
        data = {'no':i , 'id':di[0],'TipoDato':di[2],'valor':di[1],'entorno':di[3], 'linea':di[4], 'columna':[5]} 
        json_data.append(data)
        i = i+1
        
    return {"valores":json_data}

# @app.route('/getTS')
# def getTabla2():
#     reporteTS
#     print("ESTA ES LA LISTA DE TS: " + str(reporteTS))
#     return json.dumps({'reporte':reporteTS})

def getValores(anterior):
    actual = []
    for x in anterior:
        print(str(x)+" equis")
        a = x
        if isinstance(a, List):
            value = getValores(a)
            actual.append(value)
        elif isinstance(a, Dict):
            value = getValores2(a)
            actual.append(value)
        else:
            actual.append(x)
    return actual

def getValores2( dict):
    val = "("
    for x in dict:
        a = dict[x].getValor()
        if isinstance(a, List):
            value = getValores(a)
            val += str(value) + ", "
        elif isinstance(a, Dict):
            value = getValores2(a)
            val += str(value) + ", "
        else:
            val += str(dict[x].getValor()) + ", "
    val = val[:-2]  
    val += ")"
    return val

def getTipo(tipo):
    if tipo == TIPO.ENTERO:
        return "Int64"
    if tipo == TIPO.STRING:
        return "String"
    if tipo == TIPO.CHAR:
        return "Char"
    if tipo == TIPO.FLOAT:
        return "Float64"
    if tipo == TIPO.BOOL:
        return "Bool"
    if tipo == TIPO.NULO:
        return "nothing"

def agregarNativas(ast):
    instrucciones = []

    nombre = "toUpperCase"
    parametro = [{'tipo':'any', 'id':'toUpperCase##Param1'}]
    toUpperCase = ToUpperCase(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(toUpperCase)

    nombre = "typeof"
    parametro = [{'tipo':'any', 'id':'typeof##Param1'}]
    typeof = Typeof(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(typeof)

    nombre = "toLowerCase"
    parametro = [{'tipo':'any', 'id':'toLower##Param1'}]
    toLowerCase = ToLowerCase(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(toLowerCase)

    nombre = "toString"
    parametro = [{'tipo':'any', 'id':'toString##Param1'}]
    toString = String(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(toString)

    nombre = "toFixed"
    parametro = [{'tipo':'any', 'id':'toFixed##Param1'},{'tipo':'any', 'id':'toFixed##Param2'}]
    toFixed = ToFixed(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(toFixed)

    nombre = "toExponential"
    parametro = [{'tipo':'any', 'id':'toExponential##Param1'},{'tipo':'any', 'id':'toExponential##Param2'}]
    toExponential = ToExponential(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(toExponential)

    nombre = "split"
    parametro = [{'tipo':'any', 'id':'split##Param1'},{'tipo':'any', 'id':'split##Param2'}]
    split = Split(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(split)

    nombre = "concat"
    parametro = [{'tipo':'any', 'id':'concat##Param1'},{'tipo':'any', 'id':'concat##Param2'}]
    toString = Concat(nombre, parametro, instrucciones, -1,-1)
    ast.setFunciones(toString)


if __name__ == '__main__':
    app.run(debug = True, port=8080)