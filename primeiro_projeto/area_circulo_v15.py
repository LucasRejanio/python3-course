#!/usr/bin/python3
from math import pi
import sys


class TerminalColor:
    erro = '\033[91m'
    normal = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("""\
            É necessário informar o raio do círculo.
            Sintaxe: {} <raio>""".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    # Validando se o parametro é um valor númerico
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.erro + """\
            O raio deve ser um valor númerico!""" + TerminalColor.normal)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo:', area)
