
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftCOMPAREDIFERENTEleftMENORMAYORMAYORIGUALMENORIGUALleftMASMENOSCOMAleftPORDIVMODleftPARIPARDrightPOTENCIArightUMENOSAND CADENA COMA COMILLADOBLE COMILLASIMPLE COMPARE CORDER CORIZQ DECIMAL DIFERENTE DIV DPUNTOS ENTERO ID IGUAL LLAVEDER LLAVEIZQ MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MOD NOT OR PARD PARI POR POTENCIA PTCOMA PUNTO RANY RBOOLEAN RBREAK RCONSOLE RCONTINUE RELSE RFALSE RFOR RFUNCTION RIF RINTERFACE RLET RLOG RNULL RNUMBER ROF RRETURN RSTRING RTRUE RWHILEinit : instruccionesinstrucciones    : instrucciones instruccioninstrucciones : instruccioninstruccion  : imprimir puntoycoma\n                    | declaracion_normal puntoycoma\n                    | asignacion puntoycoma\n                    | condicional_ifs puntoycoma\n                    | cliclo_for puntoycoma\n                    | ciclo_while puntoycoma\n                    | funcion puntoycoma\n                    | llamada_funcion puntoycoma\n                    | r_return puntoycoma\n                    | asignaArreglo puntoycoma\n                    puntoycoma   : PTCOMA\n                    | imprimir : RCONSOLE PUNTO RLOG PARI listaExpresion PARDlistaExpresion  : listaExpresion COMA expresionlistaExpresion   : expresiondeclaracion_normal : RLET ID DPUNTOS tipodeclaracion_normal : RLET ID DPUNTOS tipo IGUAL expresiontipo : RSTRING\n            | RNUMBER\n            | RBOOLEANdeclaracion_normal : RLET ID IGUAL expresionasignacion : ID IGUAL expresioncondicional_ifs : RIF condicional_ifcondicional_if : PARI expresion PARD LLAVEIZQ instrucciones LLAVEDERcondicional_if : PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER RELSE LLAVEIZQ instrucciones LLAVEDERcondicional_if : PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER RELSE RIF condicional_ifcliclo_for : RFOR PARI declaracion_for PTCOMA expresion PTCOMA expresion PARD LLAVEIZQ instrucciones LLAVEDERcliclo_for : RFOR PARI RLET ID ROF expresion PARD LLAVEIZQ instrucciones LLAVEDERdeclaracion_for  : declaracion_normaldeclaracion_for  : IDciclo_while  : RWHILE PARI expresion PARD LLAVEIZQ instrucciones LLAVEDERfuncion  : RFUNCTION ID PARI PARD LLAVEIZQ instrucciones LLAVEDER\n                | RFUNCTION ID PARI parametros PARD LLAVEIZQ instrucciones LLAVEDERllamada_funcion  : ID PARI PARD\n                        | ID PARI parametros_ll PARDparametros : parametros COMA parametroparametros : parametroparametro    : RLET ID DPUNTOS tipo  \n                    | ID DPUNTOS tipo\n                    | IDparametros_ll : parametros_ll COMA parametro_llparametros_ll : parametro_llparametro_ll : expresionr_return : RRETURN expresionexpresion : expresion MAS expresion\n                | expresion MENOS expresion\n                | expresion POR expresion\n                | expresion DIV expresion\n                | expresion MOD expresion\n                | expresion POTENCIA expresion\n                | expresion COMPARE expresion\n                | expresion DIFERENTE expresion\n                | expresion MAYOR expresion\n                | expresion MENOR expresion\n                | expresion MAYORIGUAL expresion\n                | expresion MENORIGUAL expresion\n                | expresion AND expresion\n                | expresion OR expresion\n                expresion : MENOS expresion %prec UMENOS\n                | NOT expresion %prec UNOTexpresion : PARI expresion PARDexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : RTRUE\n                | RFALSEexpresion : expresion MAS MAS\n                | expresion MENOS MENOSexpresion : llamada_funcionexpresion : CORIZQ listaExpresion CORDERexpresion : ID listaindicesasignaArreglo    : ID listaindices IGUAL expresionlistaindices   : listaindices CORIZQ expresion CORDERlistaindices   : CORIZQ expresion CORDER'
    
_lr_action_items = {'RCONSOLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,148,149,150,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[14,14,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,14,14,14,-16,-20,14,14,14,14,-27,-34,-35,14,14,-36,14,14,14,14,-29,14,-31,-28,-30,]),'RLET':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,42,45,49,50,51,52,53,54,55,60,61,74,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,145,148,149,150,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[15,15,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,70,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,114,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,15,15,15,114,-16,-20,15,15,15,15,-27,-34,-35,15,15,-36,15,15,15,15,-29,15,-31,-28,-30,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,20,21,22,23,24,25,26,27,28,29,30,31,32,33,36,37,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,65,66,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,95,96,97,98,99,100,101,102,103,105,107,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,138,140,141,143,145,148,149,150,151,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[16,16,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,35,44,49,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,49,49,49,-26,49,71,49,-47,49,49,49,-65,-66,-67,-68,-69,-70,-73,49,49,-25,-37,49,49,108,110,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-62,-63,-75,49,-19,-21,-22,-23,-24,-38,49,-76,-78,49,146,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,49,49,-77,16,49,16,16,110,-16,-20,16,49,16,16,16,-27,-34,-35,16,16,-36,16,16,16,16,-29,16,-31,-28,-30,]),'RIF':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,148,149,150,153,155,156,159,162,163,164,166,168,169,170,172,173,174,175,176,177,178,179,],[17,17,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,17,17,17,-16,-20,17,17,17,17,-27,-34,-35,17,171,17,-36,17,17,17,17,-29,17,-31,-28,-30,]),'RFOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,148,149,150,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[18,18,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,18,18,18,-16,-20,18,18,18,18,-27,-34,-35,18,18,-36,18,18,18,18,-29,18,-31,-28,-30,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,148,149,150,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[19,19,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,19,19,19,-16,-20,19,19,19,19,-27,-34,-35,19,19,-36,19,19,19,19,-29,19,-31,-28,-30,]),'RFUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,148,149,150,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[20,20,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,20,20,20,-16,-20,20,20,20,20,-27,-34,-35,20,20,-36,20,20,20,20,-29,20,-31,-28,-30,]),'RRETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,138,141,143,148,149,150,153,155,156,159,162,163,164,168,169,170,172,173,174,175,176,177,178,179,],[21,21,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,21,21,21,-16,-20,21,21,21,21,-27,-34,-35,21,21,-36,21,21,21,21,-29,21,-31,-28,-30,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,148,149,159,162,163,169,175,177,178,179,],[0,-1,-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,-16,-20,-27,-34,-35,-36,-29,-31,-28,-30,]),'LLAVEDER':([3,4,5,6,7,8,9,10,11,12,13,22,23,24,25,26,27,28,29,30,31,32,33,40,45,49,50,51,52,53,54,55,60,61,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,148,149,150,153,155,159,162,163,164,169,173,174,175,176,177,178,179,],[-3,-15,-15,-15,-15,-15,-15,-15,-15,-15,-15,-2,-4,-14,-5,-6,-7,-8,-9,-10,-11,-12,-13,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,-16,-20,159,162,163,-27,-34,-35,169,-36,177,178,-29,179,-31,-28,-30,]),'PTCOMA':([4,5,6,7,8,9,10,11,12,13,40,45,49,50,51,52,53,54,55,60,61,69,71,72,89,90,92,96,97,98,99,100,101,103,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,148,149,159,162,163,169,175,177,178,179,],[24,24,24,24,24,24,24,24,24,24,-26,-47,-65,-66,-67,-68,-69,-70,-73,-25,-37,107,-33,-32,-62,-63,-75,-19,-21,-22,-23,-24,-38,-76,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,151,-16,-20,-27,-34,-35,-36,-29,-31,-28,-30,]),'PUNTO':([14,],[34,]),'IGUAL':([16,35,38,96,97,98,99,105,108,137,],[36,59,65,135,-21,-22,-23,-78,59,-77,]),'PARI':([16,17,18,19,21,36,37,39,41,43,44,46,47,48,49,56,57,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,171,],[37,41,42,43,48,48,48,48,48,48,74,48,48,48,37,48,95,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,41,]),'CORIZQ':([16,21,36,37,38,39,41,43,46,47,48,49,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,92,95,102,105,107,118,133,135,137,140,151,],[39,56,56,56,66,56,56,56,56,56,56,39,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,66,56,56,-78,56,56,56,56,-77,56,56,]),'MENOS':([21,36,37,39,41,43,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,64,65,66,67,68,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,95,100,101,102,103,104,105,107,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,135,137,139,140,147,149,151,152,160,],[46,46,46,46,46,46,76,46,46,46,-65,-66,-67,-68,-69,-70,-73,46,46,76,-37,76,46,46,76,76,76,46,118,46,46,46,46,46,46,46,46,46,46,46,46,-62,76,76,-75,76,46,76,-38,46,76,76,-78,46,-48,-71,-49,-72,-50,-51,-52,-53,76,76,76,76,76,76,76,76,-64,-74,46,46,-77,76,46,76,76,46,76,76,]),'NOT':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'ENTERO':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'DECIMAL':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'CADENA':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'RTRUE':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'RFALSE':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'RLOG':([34,],[57,]),'DPUNTOS':([35,108,110,146,],[58,58,142,158,]),'PARD':([37,49,50,51,52,53,54,55,61,62,63,64,68,73,74,89,90,91,92,94,97,98,99,101,105,110,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,136,137,147,152,154,157,160,165,],[61,-65,-66,-67,-68,-69,-70,-73,-37,101,-45,-46,106,109,111,-62,-63,131,-75,-18,-21,-22,-23,-38,-78,-43,144,-40,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,148,-44,-77,-17,161,-42,-39,167,-41,]),'MAS':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,75,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[75,-65,-66,-67,-68,-69,-70,-73,75,-37,75,75,75,75,116,-62,75,75,-75,75,75,-38,75,75,-78,-48,-71,-49,-72,-50,-51,-52,-53,75,75,75,75,75,75,75,75,-64,-74,-77,75,75,75,75,75,]),'POR':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[77,-65,-66,-67,-68,-69,-70,-73,77,-37,77,77,77,77,-62,77,77,-75,77,77,-38,77,77,-78,77,-71,77,-72,-50,-51,-52,-53,77,77,77,77,77,77,77,77,-64,-74,-77,77,77,77,77,77,]),'DIV':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[78,-65,-66,-67,-68,-69,-70,-73,78,-37,78,78,78,78,-62,78,78,-75,78,78,-38,78,78,-78,78,-71,78,-72,-50,-51,-52,-53,78,78,78,78,78,78,78,78,-64,-74,-77,78,78,78,78,78,]),'MOD':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[79,-65,-66,-67,-68,-69,-70,-73,79,-37,79,79,79,79,-62,79,79,-75,79,79,-38,79,79,-78,79,-71,79,-72,-50,-51,-52,-53,79,79,79,79,79,79,79,79,-64,-74,-77,79,79,79,79,79,]),'POTENCIA':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[80,-65,-66,-67,-68,-69,-70,-73,80,-37,80,80,80,80,-62,80,80,-75,80,80,-38,80,80,-78,80,-71,80,-72,80,80,80,80,80,80,80,80,80,80,80,80,-64,-74,-77,80,80,80,80,80,]),'COMPARE':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[81,-65,-66,-67,-68,-69,-70,-73,81,-37,81,81,81,81,-62,81,81,-75,81,81,-38,81,81,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,81,81,-64,-74,-77,81,81,81,81,81,]),'DIFERENTE':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[82,-65,-66,-67,-68,-69,-70,-73,82,-37,82,82,82,82,-62,82,82,-75,82,82,-38,82,82,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,82,82,-64,-74,-77,82,82,82,82,82,]),'MAYOR':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[83,-65,-66,-67,-68,-69,-70,-73,83,-37,83,83,83,83,-62,83,83,-75,83,83,-38,83,83,-78,-48,-71,-49,-72,-50,-51,-52,-53,83,83,-56,-57,-58,-59,83,83,-64,-74,-77,83,83,83,83,83,]),'MENOR':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[84,-65,-66,-67,-68,-69,-70,-73,84,-37,84,84,84,84,-62,84,84,-75,84,84,-38,84,84,-78,-48,-71,-49,-72,-50,-51,-52,-53,84,84,-56,-57,-58,-59,84,84,-64,-74,-77,84,84,84,84,84,]),'MAYORIGUAL':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[85,-65,-66,-67,-68,-69,-70,-73,85,-37,85,85,85,85,-62,85,85,-75,85,85,-38,85,85,-78,-48,-71,-49,-72,-50,-51,-52,-53,85,85,-56,-57,-58,-59,85,85,-64,-74,-77,85,85,85,85,85,]),'MENORIGUAL':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[86,-65,-66,-67,-68,-69,-70,-73,86,-37,86,86,86,86,-62,86,86,-75,86,86,-38,86,86,-78,-48,-71,-49,-72,-50,-51,-52,-53,86,86,-56,-57,-58,-59,86,86,-64,-74,-77,86,86,86,86,86,]),'AND':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[87,-65,-66,-67,-68,-69,-70,-73,87,-37,87,87,87,87,-62,-63,87,-75,87,87,-38,87,87,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,87,-64,-74,-77,87,87,87,87,87,]),'OR':([45,49,50,51,52,53,54,55,60,61,64,67,68,73,89,90,91,92,94,100,101,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,139,147,149,152,160,],[88,-65,-66,-67,-68,-69,-70,-73,88,-37,88,88,88,88,-62,-63,88,-75,88,88,-38,88,88,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,88,88,88,88,88,]),'COMA':([49,50,51,52,53,54,55,61,62,63,64,89,90,92,93,94,97,98,99,101,105,110,112,113,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,136,137,147,154,157,165,],[-65,-66,-67,-68,-69,-70,-73,-37,102,-45,-46,-62,-63,-75,133,-18,-21,-22,-23,-38,-78,-43,145,-40,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,133,-44,-77,-17,-42,-39,-41,]),'CORDER':([49,50,51,52,53,54,55,61,67,89,90,92,93,94,101,104,105,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,137,147,],[-65,-66,-67,-68,-69,-70,-73,-37,105,-62,-63,-75,132,-18,-38,137,-78,-48,-71,-49,-72,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-64,-74,-77,-17,]),'RSTRING':([58,142,158,],[97,97,97,]),'RNUMBER':([58,142,158,],[98,98,98,]),'RBOOLEAN':([58,142,158,],[99,99,99,]),'LLAVEIZQ':([106,109,111,144,161,166,167,],[138,141,143,156,168,170,172,]),'ROF':([108,],[140,]),'RELSE':([159,],[166,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,138,141,143,156,168,170,172,],[2,150,153,155,164,173,174,176,]),'instruccion':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[3,22,3,3,3,22,22,22,3,22,3,3,3,22,22,22,]),'imprimir':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion_normal':([0,2,42,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[5,5,72,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'condicional_ifs':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'cliclo_for':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ciclo_while':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'funcion':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'llamada_funcion':([0,2,21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,138,140,141,143,150,151,153,155,156,164,168,170,172,173,174,176,],[11,11,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,11,55,11,11,11,55,11,11,11,11,11,11,11,11,11,11,]),'r_return':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'asignaArreglo':([0,2,138,141,143,150,153,155,156,164,168,170,172,173,174,176,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'puntoycoma':([4,5,6,7,8,9,10,11,12,13,],[23,25,26,27,28,29,30,31,32,33,]),'listaindices':([16,49,],[38,92,]),'condicional_if':([17,171,],[40,175,]),'expresion':([21,36,37,39,41,43,46,47,48,56,59,65,66,75,76,77,78,79,80,81,82,83,84,85,86,87,88,95,102,107,118,133,135,140,151,],[45,60,64,67,68,73,89,90,91,94,100,103,104,115,117,119,120,121,122,123,124,125,126,127,128,129,130,94,64,139,89,147,149,152,160,]),'parametros_ll':([37,],[62,]),'parametro_ll':([37,102,],[63,136,]),'declaracion_for':([42,],[69,]),'listaExpresion':([56,95,],[93,134,]),'tipo':([58,142,158,],[96,154,165,]),'parametros':([74,],[112,]),'parametro':([74,145,],[113,157,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','Analizador_Sintactico.py',44),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Analizador_Sintactico.py',48),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_2','Analizador_Sintactico.py',54),
  ('instruccion -> imprimir puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',61),
  ('instruccion -> declaracion_normal puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',62),
  ('instruccion -> asignacion puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',63),
  ('instruccion -> condicional_ifs puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',64),
  ('instruccion -> cliclo_for puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',65),
  ('instruccion -> ciclo_while puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',66),
  ('instruccion -> funcion puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',67),
  ('instruccion -> llamada_funcion puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',68),
  ('instruccion -> r_return puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',69),
  ('instruccion -> asignaArreglo puntoycoma','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',70),
  ('puntoycoma -> PTCOMA','puntoycoma',1,'p_pcoma','Analizador_Sintactico.py',75),
  ('puntoycoma -> <empty>','puntoycoma',0,'p_pcoma','Analizador_Sintactico.py',76),
  ('imprimir -> RCONSOLE PUNTO RLOG PARI listaExpresion PARD','imprimir',6,'p_imprimir','Analizador_Sintactico.py',80),
  ('listaExpresion -> listaExpresion COMA expresion','listaExpresion',3,'p_imprimir_lista','Analizador_Sintactico.py',84),
  ('listaExpresion -> expresion','listaExpresion',1,'p_imprimir_lista2','Analizador_Sintactico.py',90),
  ('declaracion_normal -> RLET ID DPUNTOS tipo','declaracion_normal',4,'p_declaracion_normal2','Analizador_Sintactico.py',97),
  ('declaracion_normal -> RLET ID DPUNTOS tipo IGUAL expresion','declaracion_normal',6,'p_declaracion_normal','Analizador_Sintactico.py',101),
  ('tipo -> RSTRING','tipo',1,'p_tipo','Analizador_Sintactico.py',105),
  ('tipo -> RNUMBER','tipo',1,'p_tipo','Analizador_Sintactico.py',106),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','Analizador_Sintactico.py',107),
  ('declaracion_normal -> RLET ID IGUAL expresion','declaracion_normal',4,'p_declaracion_normal3','Analizador_Sintactico.py',111),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_asignacion','Analizador_Sintactico.py',115),
  ('condicional_ifs -> RIF condicional_if','condicional_ifs',2,'p_condicional_ifs','Analizador_Sintactico.py',119),
  ('condicional_if -> PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER','condicional_if',6,'p_condicional_if','Analizador_Sintactico.py',123),
  ('condicional_if -> PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER RELSE LLAVEIZQ instrucciones LLAVEDER','condicional_if',10,'p_condicional_if_else','Analizador_Sintactico.py',127),
  ('condicional_if -> PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER RELSE RIF condicional_if','condicional_if',9,'p_condicional_if_else_if','Analizador_Sintactico.py',131),
  ('cliclo_for -> RFOR PARI declaracion_for PTCOMA expresion PTCOMA expresion PARD LLAVEIZQ instrucciones LLAVEDER','cliclo_for',11,'p_ciclo_for','Analizador_Sintactico.py',135),
  ('cliclo_for -> RFOR PARI RLET ID ROF expresion PARD LLAVEIZQ instrucciones LLAVEDER','cliclo_for',10,'p_ciclo_for2','Analizador_Sintactico.py',139),
  ('declaracion_for -> declaracion_normal','declaracion_for',1,'p_declaracion_for','Analizador_Sintactico.py',144),
  ('declaracion_for -> ID','declaracion_for',1,'p_declaracion_for_id','Analizador_Sintactico.py',148),
  ('ciclo_while -> RWHILE PARI expresion PARD LLAVEIZQ instrucciones LLAVEDER','ciclo_while',7,'p_ciclo_while','Analizador_Sintactico.py',152),
  ('funcion -> RFUNCTION ID PARI PARD LLAVEIZQ instrucciones LLAVEDER','funcion',7,'p_funcion','Analizador_Sintactico.py',156),
  ('funcion -> RFUNCTION ID PARI parametros PARD LLAVEIZQ instrucciones LLAVEDER','funcion',8,'p_funcion','Analizador_Sintactico.py',157),
  ('llamada_funcion -> ID PARI PARD','llamada_funcion',3,'p_llamada_funcion','Analizador_Sintactico.py',165),
  ('llamada_funcion -> ID PARI parametros_ll PARD','llamada_funcion',4,'p_llamada_funcion','Analizador_Sintactico.py',166),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros','Analizador_Sintactico.py',175),
  ('parametros -> parametro','parametros',1,'p_parametros_2','Analizador_Sintactico.py',180),
  ('parametro -> RLET ID DPUNTOS tipo','parametro',4,'p_parametro','Analizador_Sintactico.py',184),
  ('parametro -> ID DPUNTOS tipo','parametro',3,'p_parametro','Analizador_Sintactico.py',185),
  ('parametro -> ID','parametro',1,'p_parametro','Analizador_Sintactico.py',186),
  ('parametros_ll -> parametros_ll COMA parametro_ll','parametros_ll',3,'p_parametros_ll','Analizador_Sintactico.py',196),
  ('parametros_ll -> parametro_ll','parametros_ll',1,'p_parametros_ll_2','Analizador_Sintactico.py',201),
  ('parametro_ll -> expresion','parametro_ll',1,'p_parametro_ll','Analizador_Sintactico.py',205),
  ('r_return -> RRETURN expresion','r_return',2,'p_return','Analizador_Sintactico.py',209),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',214),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',215),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',216),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',217),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',218),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',219),
  ('expresion -> expresion COMPARE expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',220),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',221),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',222),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',223),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',224),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',225),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',226),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',227),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','Analizador_Sintactico.py',259),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','Analizador_Sintactico.py',260),
  ('expresion -> PARI expresion PARD','expresion',3,'p_parentesis','Analizador_Sintactico.py',268),
  ('expresion -> ID','expresion',1,'p_identificador','Analizador_Sintactico.py',272),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Analizador_Sintactico.py',276),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Analizador_Sintactico.py',280),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','Analizador_Sintactico.py',284),
  ('expresion -> RTRUE','expresion',1,'p_expresion_boolean','Analizador_Sintactico.py',288),
  ('expresion -> RFALSE','expresion',1,'p_expresion_boolean','Analizador_Sintactico.py',289),
  ('expresion -> expresion MAS MAS','expresion',3,'p_expresion_incrementable','Analizador_Sintactico.py',296),
  ('expresion -> expresion MENOS MENOS','expresion',3,'p_expresion_incrementable','Analizador_Sintactico.py',297),
  ('expresion -> llamada_funcion','expresion',1,'p_expresion_funcion','Analizador_Sintactico.py',306),
  ('expresion -> CORIZQ listaExpresion CORDER','expresion',3,'p_expresion_arreglo','Analizador_Sintactico.py',310),
  ('expresion -> ID listaindices','expresion',2,'p_arreglos_operacion','Analizador_Sintactico.py',314),
  ('asignaArreglo -> ID listaindices IGUAL expresion','asignaArreglo',4,'p_arreglos_operacion2','Analizador_Sintactico.py',319),
  ('listaindices -> listaindices CORIZQ expresion CORDER','listaindices',4,'p_lista_indices','Analizador_Sintactico.py',323),
  ('listaindices -> CORIZQ expresion CORDER','listaindices',3,'p_lista_indices2','Analizador_Sintactico.py',329),
]