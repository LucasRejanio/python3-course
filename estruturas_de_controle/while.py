#!/usr/bin/python3
# Modulo para gera um valor aleatorio
from random import randint

numero_informados = -1
numero_secreto = randint(0, 9)

while numero_informados != numero_secreto:
    numero_informados = int(input('Informe o número: '))
    print('Número diferente, tente novamente!')

print('Número secreto {} foi encontrado!'.format(numero_secreto))
