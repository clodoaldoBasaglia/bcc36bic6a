# -*- Coding: UTF-8 -*-
import ply.lex as lex
import sys, io


class Lexica:
    def __init__(self):
        self.lexer = lex.lex(debug=False, module=self)

    reservadas = {
        'inteiro': 'INTEIRO',
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
                 'SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO', 'IGUALDADE', 'MAIOR', 'MENOR', 'MAIOR_IGUAL',
                 'MENOR_IGUAL', 'ABRE_PAR', 'FECHA_PAR', 'ABRE_COL', 'FECHA_COL', 'IDENTIFICADOR', 'NEGACAO',
                 'DOIS_PONTOS', 'ATRIBUICAO', 'VIRGULA','ABRE_CHAVES','FECHA_CHAVES','COMENTARIO','NOTACAO_CIENTIFICA'
             ] + list(reservadas.values())

    t_ABRE_CHAVES=r'\{'
    t_FECHA_CHAVES = r'\}'
    t_SOMA = r'\+'
    t_SUBTRACAO = '-'
    t_MULTIPLICACAO = '\*'
    t_DIVISAO = r'\/'
    t_IGUALDADE = r'\='
    t_MAIOR = r'\>'
    t_MENOR = r'\<'
    t_MAIOR_IGUAL = r'>='
    t_MENOR_IGUAL = r'<='
    t_ABRE_PAR = r'\('
    t_FECHA_PAR = r'\)'
    t_ABRE_COL = r'\['
    t_FECHA_COL = r'\]'
    t_NEGACAO = r'!'
    t_DOIS_PONTOS = r':'
    t_ATRIBUICAO = r':\='
    t_VIRGULA = r'\,'
    t_ignore = ' \t'

    def t_IDENTIFICADOR(self, t):
        r'[a-zA-Zà-ú][0-9_a-zà-úA-Z]*'
        t.type = self.reservadas.get(t.value, 'IDENTIFICADOR')
        return t

    def t_INTEIRO(self, t):
        r'[+|-]?\d+'
        t.type = self.reservadas.get(t.value, 'INTEIRO')
        return t

    def t_FLUTUANTE(self,t):
        r'\d+\.\d+'
        t.type= self.reservadas.get(t.value,'FLUTUANTE')
        return t

    def t_NOTACAO_CIENTIFICA(self, t):
        r'[+|-]?[0-9]+(\.[0-9]+)(e(\+|\-)?(\d+))?'
        t.type = self.reservadas.get(t.value, 'NOTACAO_CIENTIFICA')
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
            print(t)


def main():
    print("Lexicanum")
    codigo = io.open(sys.argv[1], mode='r', encoding="utf-8")
    adeptus = Lexica()
    adeptus.test(codigo.read())
main()
