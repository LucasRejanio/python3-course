#!/usr/bin/python3

# utilizando with, usado para garantir finalização de recursos adquiridos.
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo já foi fechado')
