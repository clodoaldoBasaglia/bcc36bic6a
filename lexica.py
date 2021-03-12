# -*- Coding: UTF-8 -*-
import ply.lex as lex
import sys
import io


class Lexica:
    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self)

    reservadas = {
        'se': 'SE',
        'então': 'ENTAO',
        'senão': 'SENAO',
        'fim': 'FIM',
        'repita': 'REPITA',
        'flutuante': 'FLUTUANTE',
        'retorna': 'RETORNA',
        'até': 'ATE',
        'leia': 'LEIA',
        'escreva': 'ESCREVA',
        'inteiro': 'INTEIRO'
#        'principal': 'PRINCIPAL'
    }
    tokens = [
        'MAIS',
        'MENOS',
        'MULTIPLICACAO',
        'DIVISAO',
        'DOIS_PONTOS',
        'VIRGULA',
        'MENOR',
        'MAIOR',
        'IGUAL',
        'DIFERENTE',
        'MAIOR_IGUAL',
        'MENOR_IGUAL',
        'E_LOGICO',
        'OU_LOGICO',
        'NEGACAO',
        'ABRE_PARENTESE',
        'FECHA_PARENTESE',
        'ABRE_COLCHETE',
        'FECHA_COLCHETE',
        'ATRIBUICAO',
        'NUM_INTEIRO',
        'NUM_PONTO_FLUTUANTE',
        'NUM_NOTACAO_CIENTIFICA',
        'ID',
        'ABRE_CHAVES',
        'FECHA_CHAVES',
        'COMENTARIO'
    ] + list(reservadas.values())

    t_MAIS = r'\+'
    t_MENOS = '-'
    t_DIVISAO = r'/'
    t_MULTIPLICACAO = '\*'
    t_VIRGULA = r','
    t_DOIS_PONTOS = r':'
    t_MAIOR = r'>'
    t_MENOR = r'<'
    t_IGUAL = r'='
    t_DIFERENTE = r'<>'
    t_MAIOR_IGUAL = r'>='
    t_MENOR_IGUAL = r'<='
    t_E_LOGICO = '&&'
    t_OU_LOGICO = '\|\|'
    t_NEGACAO = r'!'
    t_ABRE_PARENTESE = r'\('
    t_FECHA_PARENTESE = r'\)'
    t_ABRE_COLCHETE = r'\['
    t_FECHA_COLCHETE = r'\]'
    t_ATRIBUICAO = r':\='
    t_ABRE_CHAVES = r'{'
    t_FECHA_CHAVES = r'}'
    t_ignore = ' \t'




    def t_ID(self, t):
        r'[a-zA-Zà-ú][0-9_a-zà-úA-Z]*'
        t.type = self.reservadas.get(t.value, 'ID')
        return t

    def t_NUM_PONTO_FLUTUANTE(self, t):
        r'\d+\.?\d*e(\+|-)?\d+'
        t.type = self.reservadas.get(t.value, 'FLUTUANTE')
        return t

    def t_NUM_INTEIRO(self, t):
        r'[+|-]?\d+'
        t.type = self.reservadas.get(t.value, 'NUM_INTEIRO')
        return t

    def t_NUM_NOTACAO_CIENTIFICA(self, t):
        r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d*)([eE][-+]?\d+)?'
        t.type = self.reservadas.get(t.value, 'NUM_NOTACAO_CIENTIFICA')
        return t

    def t_COMENTARIO(self, t):
        r'{[\d\D]*?}'
        t.type = self.reservadas.get(t.value, 'COMENTARIO')
        return t

    def t_NEW_LINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print("Erro '%s', linha %d" % (t.value[0], t.lineno))
        print(type(t.value))
        exit(0)

    def test(self, codigo):
        lex.input(codigo)
        while True:
            t = lex.token()
            if not t:
                break
            print(t.type)


def main():
    codigo = io.open(sys.argv[1], mode='r', encoding="utf-8")
    adeptus = Lexica()
    adeptus.test(codigo.read())


main()
