#!/usr/bin/python3

# open(), metodo de acesso ao arquivo
arquivo = open('pessoas.csv')
# read(), metodo de leitura
dados = arquivo.read()
arquivo.close()

# splitlines(), metodo que separa as linhas do arquivo
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
