#!/usr/bin/python3

# strip(), metodo para tirar os espaços ou caracteres
arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
