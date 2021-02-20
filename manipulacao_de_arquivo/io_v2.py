#!/usr/bin/python3

# open(), metodo de acesso ao arquivo
arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

arquivo.close()
