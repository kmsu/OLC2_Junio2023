# CORS -> Cross Origin Resource Sharing
# Si no existe el CORS, no se puede acceder a los recursos de un servidor desde otro servidor
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
    print(str(ast.getInstr()) + " esta es la Instruccion")

    
    for instruccion in ast.getInstr():
        
        #value = instruccion.interpretar(ast, TsgGlobal)
        if isinstance(instruccion, Funcion):
            ast.setFunciones(instruccion )
        
    
    for instruccion in ast.getInstr():
        if not(isinstance(instruccion, Funcion)):
            value = instruccion.interpretar(ast, TsgGlobal)
            if isinstance(value, Excepcion):
                ast.setExcepciones(value)

    global Simbolos
    Simbolos = ast.getTsglobal().getTablaG()
    consola = str(ast.getConsola())
    print('Consola: ', consola)
    if ast.excepciones != None:
        for aux in ast.excepciones:
            print('Errores', aux.toString())
    return json.dumps({'consola':consola, 'mensaje': 'Compilado :3'})

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