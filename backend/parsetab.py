
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVleftPARIPARDrightUMENOSCADENA DECIMAL DIV DPUNTOS ENTERO ID IGUAL LLAVEDER LLAVEIZQ MAS MENOS PARD PARI POR PTCOMA PUNTO RBOOLEAN RCONSOLE RELSE RFALSE RIF RLET RLOG RNUMBER RSTRING RTRUEinit : instruccionesinstrucciones    : instrucciones instruccioninstrucciones : instruccioninstruccion : imprimir PTCOMA\n                    | declaracion_normal PTCOMA\n                    | condicional_if PTCOMAimprimir : RCONSOLE PUNTO RLOG PARI expresion PARDdeclaracion_normal : RLET ID DPUNTOS tipo IGUAL expresioncondicional_if : RIF PARI expresion PARD LLAVEIZQ LLAVEDERtipo : RSTRING\n            | RNUMBER\n            | RBOOLEANexpresion : expresion MAS expresion\n                | expresion MENOS expresion\n                | expresion POR expresion\n                | expresion DIV expresionexpresion : MENOS expresion %prec UMENOSexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : RTRUE\n                | RFALSE'
    
_lr_action_items = {'RCONSOLE':([0,2,3,10,11,12,13,],[7,7,-3,-2,-4,-5,-6,]),'RLET':([0,2,3,10,11,12,13,],[8,8,-3,-2,-4,-5,-6,]),'RIF':([0,2,3,10,11,12,13,],[9,9,-3,-2,-4,-5,-6,]),'$end':([1,2,3,10,11,12,13,],[0,-1,-3,-2,-4,-5,-6,]),'PTCOMA':([4,5,6,21,22,23,24,25,26,37,41,42,43,44,45,46,47,],[11,12,13,-18,-19,-20,-21,-22,-23,-17,-13,-14,-15,-16,-7,-8,-9,]),'PUNTO':([7,],[14,]),'ID':([8,16,20,27,33,34,35,36,39,],[15,21,21,21,21,21,21,21,21,]),'PARI':([9,17,],[16,27,]),'RLOG':([14,],[17,]),'DPUNTOS':([15,],[18,]),'MENOS':([16,19,20,21,22,23,24,25,26,27,33,34,35,36,37,38,39,41,42,43,44,46,],[20,34,20,-18,-19,-20,-21,-22,-23,20,20,20,20,20,-17,34,20,-13,-14,-15,-16,34,]),'ENTERO':([16,20,27,33,34,35,36,39,],[22,22,22,22,22,22,22,22,]),'DECIMAL':([16,20,27,33,34,35,36,39,],[23,23,23,23,23,23,23,23,]),'CADENA':([16,20,27,33,34,35,36,39,],[24,24,24,24,24,24,24,24,]),'RTRUE':([16,20,27,33,34,35,36,39,],[25,25,25,25,25,25,25,25,]),'RFALSE':([16,20,27,33,34,35,36,39,],[26,26,26,26,26,26,26,26,]),'RSTRING':([18,],[29,]),'RNUMBER':([18,],[30,]),'RBOOLEAN':([18,],[31,]),'PARD':([19,21,22,23,24,25,26,37,38,41,42,43,44,],[32,-18,-19,-20,-21,-22,-23,-17,45,-13,-14,-15,-16,]),'MAS':([19,21,22,23,24,25,26,37,38,41,42,43,44,46,],[33,-18,-19,-20,-21,-22,-23,-17,33,-13,-14,-15,-16,33,]),'POR':([19,21,22,23,24,25,26,37,38,41,42,43,44,46,],[35,-18,-19,-20,-21,-22,-23,-17,35,35,35,-15,-16,35,]),'DIV':([19,21,22,23,24,25,26,37,38,41,42,43,44,46,],[36,-18,-19,-20,-21,-22,-23,-17,36,36,36,-15,-16,36,]),'IGUAL':([28,29,30,31,],[39,-10,-11,-12,]),'LLAVEIZQ':([32,],[40,]),'LLAVEDER':([40,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,10,]),'imprimir':([0,2,],[4,4,]),'declaracion_normal':([0,2,],[5,5,]),'condicional_if':([0,2,],[6,6,]),'expresion':([16,20,27,33,34,35,36,39,],[19,37,38,41,42,43,44,46,]),'tipo':([18,],[28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','Analizador_Sintactico.py',21),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','Analizador_Sintactico.py',25),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_2','Analizador_Sintactico.py',31),
  ('instruccion -> imprimir PTCOMA','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',38),
  ('instruccion -> declaracion_normal PTCOMA','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',39),
  ('instruccion -> condicional_if PTCOMA','instruccion',2,'p_instrucciones_evaluar','Analizador_Sintactico.py',40),
  ('imprimir -> RCONSOLE PUNTO RLOG PARI expresion PARD','imprimir',6,'p_imprimir','Analizador_Sintactico.py',44),
  ('declaracion_normal -> RLET ID DPUNTOS tipo IGUAL expresion','declaracion_normal',6,'p_declaracion_normal','Analizador_Sintactico.py',48),
  ('condicional_if -> RIF PARI expresion PARD LLAVEIZQ LLAVEDER','condicional_if',6,'p_condicional_if','Analizador_Sintactico.py',52),
  ('tipo -> RSTRING','tipo',1,'p_tipo','Analizador_Sintactico.py',57),
  ('tipo -> RNUMBER','tipo',1,'p_tipo','Analizador_Sintactico.py',58),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','Analizador_Sintactico.py',59),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',63),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',64),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',65),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','Analizador_Sintactico.py',66),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','Analizador_Sintactico.py',77),
  ('expresion -> ID','expresion',1,'p_identificador','Analizador_Sintactico.py',81),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Analizador_Sintactico.py',85),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Analizador_Sintactico.py',89),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','Analizador_Sintactico.py',93),
  ('expresion -> RTRUE','expresion',1,'p_expresion_boolean','Analizador_Sintactico.py',97),
  ('expresion -> RFALSE','expresion',1,'p_expresion_boolean','Analizador_Sintactico.py',98),
]