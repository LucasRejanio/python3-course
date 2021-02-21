#!/usr/bin/python3
import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando arquivo CSV...')
        dados = entrada.read().decode('latin1')
        print('Do2nload completo!')

        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    url = 'http://files.cod3r.com.br/curso-python/desafio-ibge.csv'
    read(url)
