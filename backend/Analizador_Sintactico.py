from src.Instrucciones.llamada_funcion import Llamada_Funcion
from src.Instrucciones.funcion import Funcion
from src.Instrucciones.ciclo_for import For
from src.Instrucciones.ciclo_forOf import ForOf
from src.Instrucciones.ciclo_while import CWhile
from src.Instrucciones.condicional_if import If
from src.Expresiones.relacional_logica import Relacional_Logica
from src.Expresiones.identificador import Identificador
from src.Tabla_Simbolos.arbol import Arbol
from src.Tabla_Simbolos.excepcion import Excepcion
import ply.yacc as yacc
from Analizador_Lexico import tokens, lexer, errores, find_column
from src.Expresiones.aritmetica import Aritmetica
from src.Expresiones.primitivos import Primitivos
from src.Instrucciones.imprimir import Imprimir
from src.Instrucciones.declaracion_variables import Declaracion_Variables
from src.Instrucciones.asignacion import Asignacion
from src.Tabla_Simbolos.tabla_simbolos import TablaSimbolos
# pip freeze > requirements.txt para crear el archivo de requerimientos 
# pip install -r requirements.txt para instalar los requerimientos del archivo requirements.txt
# Definicion de la jerarquia de operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right','UNOT'),
    ('left', 'COMPARE', 'DIFERENTE'),
    ('left', 'MENOR', 'MAYOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV', 'MOD'),
    ('left','PARI', 'PARD'),
    ('right','UMENOS'),
    )

# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2(t):
    'instrucciones : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instrucciones_evaluar(t):
    '''instruccion  : imprimir puntoycoma
                    | declaracion_normal puntoycoma
                    | asignacion puntoycoma
                    | condicional_ifs puntoycoma
                    | cliclo_for puntoycoma
                    | ciclo_while puntoycoma
                    | funcion puntoycoma
                    | llamada_funcion puntoycoma
                    '''
    t[0] = t[1]

def p_pcoma(t):
    '''puntoycoma   : PTCOMA
                    | '''
    pass

def p_imprimir(t):
    'imprimir : RCONSOLE PUNTO RLOG PARI listaExpresion PARD'
    t[0] = Imprimir(t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_imprimir_lista(t):
    'listaExpresion  : listaExpresion COMA expresion'
    if t[3] != "":
        t[1].append(t[3])
    t[0] = t[1]

def p_imprimir_lista2(t):
    'listaExpresion   : expresion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_declaracion_normal(t):
    'declaracion_normal : RLET ID DPUNTOS tipo IGUAL expresion'
    t[0] = Declaracion_Variables(t[2], t[4], t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_normal2(t):
    'declaracion_normal : RLET ID IGUAL expresion'
    t[0] = Declaracion_Variables(t[2], None, t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_asignacion(t):
    'asignacion : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1])) 

def p_condicional_ifs(t):
    'condicional_ifs : RIF condicional_if'
    t[0] = t[2]

def p_condicional_if(t):
    'condicional_if : PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER'
    t[0] = If(t[2], t[5], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicional_if_else(t):
    'condicional_if : PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER RELSE LLAVEIZQ instrucciones LLAVEDER'
    t[0] = If(t[2], t[5], t[9], None, t.lineno(1), find_column(input, t.slice[1]))

def p_condicional_if_else_if(t):
    'condicional_if : PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER RELSE RIF condicional_if'
    t[0] = If(t[2], t[5], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

def p_ciclo_for(t):
    'cliclo_for : RFOR PARI declaracion_for PTCOMA expresion PTCOMA expresion PARD LLAVEIZQ instrucciones LLAVEDER'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), find_column(input, t.slice[1]))

def p_ciclo_for2(t):
    'cliclo_for : RFOR PARI RLET ID ROF expresion PARD LLAVEIZQ instrucciones LLAVEDER'
    declaraId = Declaracion_Variables(t[4], None, None, t.lineno(1), find_column(input, t.slice[1]))
    t[0] = ForOf(declaraId, t[6], t[9], t.lineno(1), find_column(input, t.slice[1]))
    
def p_declaracion_for(t):
    'declaracion_for  : declaracion_normal'
    t[0] = t[1]

def p_declaracion_for_id(t):
    'declaracion_for  : ID'
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]), None)

def p_ciclo_while(t):
    'ciclo_while  : RWHILE PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER'
    t[0] = CWhile(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))   

def p_funcion(t):
    'funcion : RFUNCTION ID PARI PARD LLAVEIZQ instrucciones LLAVEDER'
    t[0] = Funcion(t[2],None,t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada_funcion(t):
    'llamada_funcion : ID PARI PARD'
    t[0] = Llamada_Funcion(t[1],None,t.lineno(1), find_column(input, t.slice[1]))

def p_tipo(t):
    '''tipo : RSTRING
            | RNUMBER
            | RBOOLEAN'''
    t[0] = t[1]

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIV expresion
                | expresion MOD expresion
                | expresion POTENCIA expresion
                | expresion COMPARE expresion
                | expresion DIFERENTE expresion
                | expresion MAYOR expresion
                | expresion MENOR expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion AND expresion
                | expresion OR expresion
                '''
    if t[2] == '+'  : 
        t[0] = Aritmetica(t[1], t[3], '+', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], '-', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*': 
        t[0] = Aritmetica(t[1], t[3], '*', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmetica(t[1], t[3], '/', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%': 
        t[0] = Aritmetica(t[1], t[3], '%', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '^': 
        t[0] = Aritmetica(t[1], t[3], '^', t.lineno(2), find_column(input, t.slice[2]))    
    elif t[2] == '===':
        t[0] = Relacional_Logica(t[1], t[3], '===', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!==':
        t[0] = Relacional_Logica(t[1], t[3], '!==', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional_Logica(t[1], t[3], '>', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional_Logica(t[1], t[3], '<', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional_Logica(t[1], t[3], '>=', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional_Logica(t[1], t[3], '<=', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Relacional_Logica(t[1], t[3], '&&', t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Relacional_Logica(t[1], t[3], '||', t.lineno(2), find_column(input, t.slice[2]))
    
def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec UNOT'''
    if t[1] == '-':
        cero = Primitivos('number', 0, -1, -1)
        t[0] = Aritmetica(cero, t[2], '-', t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Relacional_Logica(t[2], None, '!', t.lineno(1), find_column(input, t.slice[1]))

def p_parentesis(t):
    'expresion : PARI expresion PARD'
    t[0] = t[2]

def p_identificador(t):
    'expresion : ID'
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]), None)

def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitivos('number', int(t[1]), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitivos('number', float(t[1]), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitivos('string', str(t[1]), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_boolean(t):
    '''expresion : RTRUE
                | RFALSE'''
    if t[1] == 'true':
        t[0] = Primitivos('boolean', True, t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Primitivos('boolean', False, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_incrementable(t):
    '''expresion : expresion MAS MAS
                | expresion MENOS MENOS'''
    if t[2] == '+':
        incrementable = Primitivos('number', 1, t.lineno(2), find_column(input, t.slice[2]))
        t[0] = Aritmetica(t[1],incrementable, '+', t.lineno(2), find_column(input, t.slice[2]))
    else:
        incrementable = Primitivos('number', 1, t.lineno(2), find_column(input, t.slice[2]))
        t[0] = Aritmetica(t[1],incrementable, '-', t.lineno(2), find_column(input, t.slice[2]))

def p_error(t):
    print(" Error sintáctico en '%s'" % t.value)

input = ''

def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

# entrada = '''
# let a : number = 5;
# let b : number = a++;

# for(let i : number = 0; i < 10; i++){
#     console.log(i);
# };

# '''

# def test_lexer(lexer):
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break  # No more input
#         print(tok)

# # lexer.input(entrada)
# # test_lexer(lexer)
# instrucciones = parse(entrada)
# ast = Arbol(instrucciones)
# tsg = TablaSimbolos()
# ast.setTsglobal(tsg)


# for instruccion in ast.getInstr():
#     value = instruccion.interpretar(ast,tsg)
#     if isinstance(value, Excepcion):
#         ast.getExcepciones().append(value)
#         ast.updateConsola(value.toString())
# print(ast.getConsola())