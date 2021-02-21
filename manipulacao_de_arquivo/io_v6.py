#!/usr/bin/python3

# utilizando modo de escrita do with para gerar
# um novo arquivo txt a partir do csv
with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado')

if arquivo.closed:
    print('Arquivo de saida já foi fechado')
