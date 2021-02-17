#!/usr/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


# Passando parametro pelo terminal
if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do circulo:', area)
