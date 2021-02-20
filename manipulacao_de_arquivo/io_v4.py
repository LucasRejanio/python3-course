#!/usr/bin/python3

# utilizando try e finally, para garantir o fechamento do recurso
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado')
