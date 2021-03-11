# -*- Coding: UTF-8 -*-
import ply.lex as lex
import sys, io


class Lexica:
    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self)

    reservadas = {
        'inteiro': 'NUM_INTEIRO',
        'flutuante': 'FLUTUANTE',
        'retorna': 'RETORNA',
        'se':'SE',
        'senão':'SENAO',
        'então':'ENTAO',
        'fim':'FIM',
        'até':'ATE',
        'repita':'REPITA',
        'principal':'PRINCIPAL',
        'leia':'LEIA',
        'escreva':'ESCREVA'
    }
    tokens = [
                 'MAIS', 'MENOS', 'MULTIPLICACAO', 'DIVISAO', 'IGUALDADE', 'MAIOR', 'MENOR', 'MAIOR_IGUAL',
                 'MENOR_IGUAL', 'ABRE_PARENTESE', 'FECHA_PARENTESE', 'ABRE_COLCHETE', 'FECHA_COLCHETE', 'ID', 'NEGACAO',
                 'DOIS_PONTOS', 'ATRIBUICAO', 'VIRGULA','ABRE_CHAVES','FECHA_CHAVES','COMENTARIO','NUM_NOTACAO_CIENTIFICA'
             ] + list(reservadas.values())

    t_ABRE_CHAVES=r'\{'
    t_FECHA_CHAVES = r'\}'
    t_MAIS = r'\+'
    t_MENOS = '-'
    t_MULTIPLICACAO = '\*'
    t_DIVISAO = r'\/'
    t_IGUALDADE = r'\='
    t_MAIOR = r'\>'
    t_MENOR = r'\<'
    t_MAIOR_IGUAL = r'>='
    t_MENOR_IGUAL = r'<='
    t_ABRE_PARENTESE = r'\('
    t_FECHA_PARENTESE = r'\)'
    t_ABRE_COLCHETE = r'\['
    t_FECHA_COLCHETE = r'\]'
    t_NEGACAO = r'!'
    t_DOIS_PONTOS = r':'
    t_ATRIBUICAO = r':\='
    t_VIRGULA = r'\,'
    t_ignore = ' \t'

    def t_ID(self, t):
        r'[a-zA-Zà-ú][0-9_a-zà-úA-Z]*'
        t.type = self.reservadas.get(t.value, 'ID')
        return t

    def t_FLUTUANTE(self,t):
        r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d*)([eE][-+]?\d+)?'
        t.type= self.reservadas.get(t.value,'FLUTUANTE')
        return t


    def t_NUM_INTEIRO(self, t):
        r'[+|-]?\d+'
        t.type = self.reservadas.get(t.value, 'NUM_INTEIRO')
        return t



    def t_NUM_NOTACAO_CIENTIFICA(self, t):
        r'[+|-]?[0-9]+(\.[0-9]+)(e(\+|\-)?(\d+))?'
        t.type = self.reservadas.get(t.value, 'NUM_NOTACAO_CIENTIFICA')
        return t

    def t_COMENTARIO(self,t):
        r'\{.*?[^\}]+\}'
        t.type = self.reservadas.get(t.value,'COMENTARIO')
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
