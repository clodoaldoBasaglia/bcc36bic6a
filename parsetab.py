
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALDADENEGACAOMENOR_IGUALMAIORMAIOR_IGUALMENORleftSOMASUBTRACAOleftMULTIPLICACAODIVISAOABRE_CHAVES ABRE_COL ABRE_PAR ATE ATRIBUICAO COMENTARIO DIVISAO DOIS_PONTOS ENTAO ESCREVA FECHA_CHAVES FECHA_COL FECHA_PAR FIM FLUTUANTE IDENTIFICADOR IGUALDADE INTEIRO LEIA MAIOR MAIOR_IGUAL MENOR MENOR_IGUAL MULTIPLICACAO NEGACAO NOTACAO_CIENTIFICA PRINCIPAL REPITA RETORNA SE SENAO SOMA SUBTRACAO VIRGULA\n        programa : lista_declaracoes\n                     \n        lista_declaracoes : lista_declaracoes declaracao\n                           | declaracao\n        \n        declaracao : declaracao_variaveis\n                    | inicializacao_variaveis\n                    | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : var VIRGULA lista_variaveis\n                        | var\n        \n        var : IDENTIFICADOR\n            | IDENTIFICADOR indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n                | ABRE_COL expressao FECHA_COL\n        \n        tipo : INTEIRO\n        \n        tipo : FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                        | cabecalho\n        \n        cabecalho : IDENTIFICADOR ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA lista_parametros\n                            | parametro\n                            | vazio\n        \n        parametro : tipo DOIS_PONTOS IDENTIFICADOR\n        \n        parametro : parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n                | vazio\n        \n        acao : expressao\n                    | declaracao_variaveis\n                    | se\n                    | repita\n                    | leia\n                    | escreva\n                    | retorna\n                    | error\n        \n            se : SE expressao ENTAO corpo FIM\n                | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            atribuicao : var ATRIBUICAO expressao\n        \n            leia : LEIA ABRE_PAR IDENTIFICADOR FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_simples\n                        | atribuicao\n        \n            expressao_simples : expressao_aditiva\n                                | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_multiplicacao expressao_unaria\n        \n           expressao_multiplicativa : expressao_unaria\n                           | expressao_multiplicativa operador_multiplicacao expressao_unaria\n        \n            expressao_unaria : fator\n                            | operador_soma fator\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUALDADE\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n                                | NEGACAO\n        \n            operador_soma : SOMA\n                    | SUBTRACAO\n        \n            operador_multiplicacao : MULTIPLICACAO\n                                    | DIVISAO\n        \n            fator : ABRE_COL  expressao FECHA_COL\n                    | var\n                    | chamada_funcao\n                    | numero\n        \n            numero : INTEIRO\n                    | FLUTUANTE\n        \n            chamada_funcao : IDENTIFICADOR ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio :\n        '
    
_lr_action_items = {'INTEIRO':([0,2,3,4,5,6,8,9,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,46,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,69,70,71,72,73,77,78,79,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,102,103,106,108,109,110,111,115,116,117,118,119,120,121,122,123,],[10,10,-3,-4,-5,-6,-8,-18,-2,-17,40,10,-12,40,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,40,40,-64,-65,-58,-59,-66,-67,40,40,-52,-53,-54,-55,-56,-57,40,-60,-61,40,40,-51,-63,-72,10,-14,-9,-45,-47,-49,-62,102,-26,-13,-68,40,-19,-25,-27,-28,-29,-30,-31,-32,-33,-34,40,-72,-66,-67,102,40,40,-72,40,102,-37,-39,-40,-41,-35,-72,102,-36,]),'FLUTUANTE':([0,2,3,4,5,6,8,9,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,46,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,69,70,71,72,73,77,78,79,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,102,103,106,108,109,110,111,115,116,117,118,119,120,121,122,123,],[11,11,-3,-4,-5,-6,-8,-18,-2,-17,41,11,-12,41,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,41,41,-64,-65,-58,-59,-66,-67,41,41,-52,-53,-54,-55,-56,-57,41,-60,-61,41,41,-51,-63,-72,11,-14,-9,-45,-47,-49,-62,103,-26,-13,-68,41,-19,-25,-27,-28,-29,-30,-31,-32,-33,-34,41,-72,-66,-67,103,41,41,-72,41,103,-37,-39,-40,-41,-35,-72,103,-36,]),'IDENTIFICADOR':([0,2,3,4,5,6,7,8,9,10,11,14,15,16,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,67,69,70,71,72,73,77,78,79,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,102,103,106,107,108,109,110,111,115,116,117,118,119,120,121,122,123,],[13,13,-3,-4,-5,-6,17,-8,-18,-15,-16,-2,24,-17,32,-12,32,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,32,32,-64,-65,-58,-59,-66,-67,32,24,32,-52,-53,-54,-55,-56,-57,32,-60,-61,32,32,-51,-63,-72,82,-14,-9,-45,-47,-49,-62,32,-26,-13,-68,32,-19,-25,-27,-28,-29,-30,-31,-32,-33,-34,32,-72,-66,-67,32,112,32,32,-72,32,32,-37,-39,-40,-41,-35,-72,32,-36,]),'$end':([1,2,3,4,5,6,8,9,14,16,20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,69,70,71,72,73,77,83,84,86,],[0,-1,-3,-4,-5,-6,-8,-18,-2,-17,-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-9,-45,-47,-49,-62,-13,-68,-19,]),'DOIS_PONTOS':([7,10,11,45,96,102,103,],[15,-15,-16,67,15,-15,-16,]),'ATRIBUICAO':([12,13,20,25,32,69,83,],[18,-11,-12,18,-11,-14,-13,]),'ABRE_PAR':([13,17,32,99,100,101,],[19,19,60,107,108,109,]),'ABRE_COL':([13,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,46,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,71,72,73,77,78,79,81,82,83,84,85,87,88,89,90,91,92,93,94,95,97,98,102,103,106,108,109,110,111,115,116,117,118,119,120,121,122,123,],[21,35,46,35,-7,-10,21,-63,-38,-42,-43,-44,-46,-48,21,-50,35,35,-64,-65,-58,-59,-66,-67,66,35,35,-52,-53,-54,-55,-56,-57,35,-60,-61,35,35,-51,-63,-72,-14,-9,-45,-47,-49,-62,35,-26,-24,-23,-13,-68,35,-25,-27,-28,-29,-30,-31,-32,-33,-34,35,-72,-66,-67,35,35,35,-72,35,35,-37,-39,-40,-41,-35,-72,35,-36,]),'SOMA':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,40,41,46,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,71,72,73,77,78,79,83,84,85,87,88,89,90,91,92,93,94,95,97,98,102,103,106,108,109,110,111,115,116,117,118,119,120,121,122,123,],[38,-12,38,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,38,-64,-65,-66,-67,38,38,-52,-53,-54,-55,-56,-57,38,-60,-61,38,38,-51,-63,-72,-14,-9,-45,-47,-49,-62,38,-26,-13,-68,38,-25,-27,-28,-29,-30,-31,-32,-33,-34,38,-72,-66,-67,38,38,38,-72,38,38,-37,-39,-40,-41,-35,-72,38,-36,]),'SUBTRACAO':([18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,40,41,46,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,69,70,71,72,73,77,78,79,83,84,85,87,88,89,90,91,92,93,94,95,97,98,102,103,106,108,109,110,111,115,116,117,118,119,120,121,122,123,],[39,-12,39,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,39,-64,-65,-66,-67,39,39,-52,-53,-54,-55,-56,-57,39,-60,-61,39,39,-51,-63,-72,-14,-9,-45,-47,-49,-62,39,-26,-13,-68,39,-25,-27,-28,-29,-30,-31,-32,-33,-34,39,-72,-66,-67,39,39,39,-72,39,39,-37,-39,-40,-41,-35,-72,39,-36,]),'FECHA_PAR':([19,20,25,26,27,28,29,30,31,32,33,36,37,40,41,42,43,44,60,61,62,65,69,71,72,73,74,75,76,77,80,81,82,83,84,104,112,113,114,],[-72,-12,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,64,-21,-22,-72,-51,-63,-72,-14,-45,-47,-49,84,-70,-71,-62,-20,-24,-23,-13,-68,-69,117,118,119,]),'VIRGULA':([19,20,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,42,43,44,60,61,62,65,69,71,72,73,74,75,76,77,80,81,82,83,84,104,],[-72,-12,48,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,65,-21,-22,-72,-51,-63,-72,-14,-45,-47,-49,85,-70,-71,-62,65,-24,-23,-13,-68,-69,]),'FIM':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,102,103,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,86,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-66,-67,-72,120,-37,-39,-40,-41,-35,-72,123,-36,]),'error':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,95,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,95,-72,95,-37,-39,-40,-41,-35,-72,95,-36,]),'SE':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,97,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,97,-72,97,-37,-39,-40,-41,-35,-72,97,-36,]),'REPITA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,98,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,98,-72,98,-37,-39,-40,-41,-35,-72,98,-36,]),'LEIA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,99,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,99,-72,99,-37,-39,-40,-41,-35,-72,99,-36,]),'ESCREVA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,100,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,100,-72,100,-37,-39,-40,-41,-35,-72,100,-36,]),'RETORNA':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,64,69,70,71,72,73,77,78,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,110,115,116,117,118,119,120,121,122,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-72,-14,-9,-45,-47,-49,-62,101,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,101,-72,101,-37,-39,-40,-41,-35,-72,101,-36,]),'ATE':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,69,70,71,72,73,77,79,83,84,87,88,89,90,91,92,93,94,95,98,102,103,106,116,117,118,119,120,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-9,-45,-47,-49,-62,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-72,-66,-67,111,-37,-39,-40,-41,-35,-36,]),'SENAO':([20,22,23,24,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,69,70,71,72,73,77,79,83,84,87,88,89,90,91,92,93,94,95,102,103,110,115,116,117,118,119,120,123,],[-12,-7,-10,-11,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-9,-45,-47,-49,-62,-26,-13,-68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-66,-67,-72,121,-37,-39,-40,-41,-35,-36,]),'MULTIPLICACAO':([20,25,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,57,57,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,57,-47,-49,-62,-13,-68,-66,-67,]),'DIVISAO':([20,25,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,58,58,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,58,-47,-49,-62,-13,-68,-66,-67,]),'MENOR':([20,25,27,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,50,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,-66,-67,]),'MAIOR':([20,25,27,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,51,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,-66,-67,]),'IGUALDADE':([20,25,27,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,52,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,-66,-67,]),'MENOR_IGUAL':([20,25,27,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,53,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,-66,-67,]),'MAIOR_IGUAL':([20,25,27,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,54,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,-66,-67,]),'NEGACAO':([20,25,27,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,102,103,],[-12,-63,55,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,-66,-67,]),'FECHA_COL':([20,25,26,27,28,29,30,31,32,33,36,37,40,41,47,61,62,63,66,68,69,71,72,73,77,83,84,],[-12,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,69,-51,-63,77,81,83,-14,-45,-47,-49,-62,-13,-68,]),'ENTAO':([20,25,26,27,28,29,30,31,32,33,36,37,40,41,61,62,69,71,72,73,77,83,84,105,],[-12,-63,-38,-42,-43,-44,-46,-48,-11,-50,-64,-65,-66,-67,-51,-63,-14,-45,-47,-49,-62,-13,-68,110,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes':([0,],[2,]),'declaracao':([0,2,],[3,14,]),'declaracao_variaveis':([0,2,78,106,115,122,],[4,4,89,89,89,89,]),'inicializacao_variaveis':([0,2,],[5,5,]),'declaracao_funcao':([0,2,],[6,6,]),'tipo':([0,2,19,65,78,106,115,122,],[7,7,45,45,96,96,96,96,]),'atribuicao':([0,2,18,21,35,46,60,78,85,97,106,108,109,111,115,122,],[8,8,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'cabecalho':([0,2,7,],[9,9,16,]),'var':([0,2,15,18,21,34,35,46,48,49,56,59,60,78,85,97,106,108,109,111,115,122,],[12,12,23,25,25,62,25,25,23,62,62,62,25,25,25,25,25,25,25,25,25,25,]),'indice':([13,24,32,],[20,20,20,]),'lista_variaveis':([15,48,],[22,70,]),'expressao':([18,21,35,46,60,78,85,97,106,108,109,111,115,122,],[26,47,63,68,75,88,104,105,88,113,114,116,88,88,]),'expressao_simples':([18,21,35,46,60,78,85,97,106,108,109,111,115,122,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'expressao_aditiva':([18,21,35,46,49,60,78,85,97,106,108,109,111,115,122,],[29,29,29,29,71,29,29,29,29,29,29,29,29,29,29,]),'expressao_multiplicativa':([18,21,35,46,49,60,78,85,97,106,108,109,111,115,122,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'expressao_unaria':([18,21,35,46,49,56,59,60,78,85,97,106,108,109,111,115,122,],[31,31,31,31,31,72,73,31,31,31,31,31,31,31,31,31,31,]),'fator':([18,21,34,35,46,49,56,59,60,78,85,97,106,108,109,111,115,122,],[33,33,61,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'operador_soma':([18,21,35,46,49,56,59,60,78,85,97,106,108,109,111,115,122,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'chamada_funcao':([18,21,34,35,46,49,56,59,60,78,85,97,106,108,109,111,115,122,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'numero':([18,21,34,35,46,49,56,59,60,78,85,97,106,108,109,111,115,122,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'lista_parametros':([19,65,],[42,80,]),'parametro':([19,65,],[43,43,]),'vazio':([19,60,64,65,98,110,121,],[44,76,79,44,79,79,79,]),'operador_relacional':([27,],[49,]),'operador_multiplicacao':([29,30,71,],[56,59,56,]),'lista_argumentos':([60,],[74,]),'corpo':([64,98,110,121,],[78,106,115,122,]),'acao':([78,106,115,122,],[87,87,87,87,]),'se':([78,106,115,122,],[90,90,90,90,]),'repita':([78,106,115,122,],[91,91,91,91,]),'leia':([78,106,115,122,],[92,92,92,92,]),'escreva':([78,106,115,122,],[93,93,93,93,]),'retorna':([78,106,115,122,],[94,94,94,94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','sintatica.py',27),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','sintatica.py',33),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','sintatica.py',34),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','sintatica.py',43),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','sintatica.py',44),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','sintatica.py',45),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','sintatica.py',51),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','sintatica.py',57),
  ('lista_variaveis -> var VIRGULA lista_variaveis','lista_variaveis',3,'p_lista_variaveis','sintatica.py',63),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','sintatica.py',64),
  ('var -> IDENTIFICADOR','var',1,'p_var','sintatica.py',73),
  ('var -> IDENTIFICADOR indice','var',2,'p_var','sintatica.py',74),
  ('indice -> indice ABRE_COL expressao FECHA_COL','indice',4,'p_indice','sintatica.py',83),
  ('indice -> ABRE_COL expressao FECHA_COL','indice',3,'p_indice','sintatica.py',84),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','sintatica.py',93),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo2','sintatica.py',99),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','sintatica.py',105),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','sintatica.py',106),
  ('cabecalho -> IDENTIFICADOR ABRE_PAR lista_parametros FECHA_PAR corpo FIM','cabecalho',6,'p_cabecalho','sintatica.py',115),
  ('lista_parametros -> lista_parametros VIRGULA lista_parametros','lista_parametros',3,'p_lista_parametros','sintatica.py',121),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','sintatica.py',122),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','sintatica.py',123),
  ('parametro -> tipo DOIS_PONTOS IDENTIFICADOR','parametro',3,'p_parametro1','sintatica.py',132),
  ('parametro -> parametro ABRE_COL FECHA_COL','parametro',3,'p_parametro2','sintatica.py',138),
  ('corpo -> corpo acao','corpo',2,'p_corpo','sintatica.py',144),
  ('corpo -> vazio','corpo',1,'p_corpo','sintatica.py',145),
  ('acao -> expressao','acao',1,'p_acao','sintatica.py',154),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','sintatica.py',155),
  ('acao -> se','acao',1,'p_acao','sintatica.py',156),
  ('acao -> repita','acao',1,'p_acao','sintatica.py',157),
  ('acao -> leia','acao',1,'p_acao','sintatica.py',158),
  ('acao -> escreva','acao',1,'p_acao','sintatica.py',159),
  ('acao -> retorna','acao',1,'p_acao','sintatica.py',160),
  ('acao -> error','acao',1,'p_acao','sintatica.py',161),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','sintatica.py',167),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','sintatica.py',168),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','sintatica.py',177),
  ('atribuicao -> var ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','sintatica.py',183),
  ('leia -> LEIA ABRE_PAR IDENTIFICADOR FECHA_PAR','leia',4,'p_leia','sintatica.py',190),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','sintatica.py',196),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','sintatica.py',202),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','sintatica.py',208),
  ('expressao -> atribuicao','expressao',1,'p_expressao','sintatica.py',209),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','sintatica.py',215),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','sintatica.py',216),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','sintatica.py',225),
  ('expressao_aditiva -> expressao_aditiva operador_multiplicacao expressao_unaria','expressao_aditiva',3,'p_expressao_aditiva','sintatica.py',226),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','sintatica.py',235),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','sintatica.py',236),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','sintatica.py',245),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','sintatica.py',246),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','sintatica.py',255),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','sintatica.py',256),
  ('operador_relacional -> IGUALDADE','operador_relacional',1,'p_operador_relacional','sintatica.py',257),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','sintatica.py',258),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','sintatica.py',259),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','sintatica.py',260),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','sintatica.py',266),
  ('operador_soma -> SUBTRACAO','operador_soma',1,'p_operador_soma','sintatica.py',267),
  ('operador_multiplicacao -> MULTIPLICACAO','operador_multiplicacao',1,'p_operador_multiplicacao','sintatica.py',273),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','sintatica.py',274),
  ('fator -> ABRE_COL expressao FECHA_COL','fator',3,'p_fator','sintatica.py',280),
  ('fator -> var','fator',1,'p_fator','sintatica.py',281),
  ('fator -> chamada_funcao','fator',1,'p_fator','sintatica.py',282),
  ('fator -> numero','fator',1,'p_fator','sintatica.py',283),
  ('numero -> INTEIRO','numero',1,'p_numero','sintatica.py',292),
  ('numero -> FLUTUANTE','numero',1,'p_numero','sintatica.py',293),
  ('chamada_funcao -> IDENTIFICADOR ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','sintatica.py',299),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','sintatica.py',305),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','sintatica.py',306),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','sintatica.py',307),
  ('vazio -> <empty>','vazio',0,'p_vazio','sintatica.py',316),
]