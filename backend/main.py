# CORS -> Cross Origin Resource Sharing
# Si no existe el CORS, no se puede acceder a los recursos de un servidor desde otro servidor
from Analizador_Sintactico import parse as Analizar
from src.Instrucciones.funcion import Funcion
from src.Expresiones.identificador import Identificador
from src.Instrucciones.llamada_funcion import Llamada_Funcion
from src.Instrucciones.imprimir import Imprimir
from src.Tabla_Simbolos.arbol import Arbol
from src.Tabla_Simbolos.excepcion import Excepcion
from src.Tabla_Simbolos.tabla_simbolos import TablaSimbolos
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
        return redirect(url_for("salida"))
    else:
        return {"mensaje": "No compilado"}

@app.route('/salida')
def salida():
    global tmp_val
    global Tabla
    Tabla = {}
    instrucciones = Analizar(tmp_val)
    ast = Arbol(instrucciones)
    TsgGlobal = TablaSimbolos()
    ast.setTsglobal(TsgGlobal)
    for error in errores:
        ast.setExcepciones(error)

    # for instruccion in ast.getInstr():
    #     value = instruccion.interpretar(ast, TsgGlobal)
    #     if isinstance(value, Excepcion):
    #         ast.setExcepciones(value)

    for instruccion in ast.getInstr():
        #value = instruccion.interpretar(ast, TsgGlobal)
        if isinstance(instruccion, Funcion):
            ast.setFunciones(instruccion)
    
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

if __name__ == '__main__':
    app.run(debug = True, port=8080)