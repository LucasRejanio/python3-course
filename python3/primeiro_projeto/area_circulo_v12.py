#!/usr/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


# Criando uma função de help
def help():
    print("""\
            É necessário informar o raio do círculo.
            Sintaxe: {} <raio>""".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do circulo:', area)
