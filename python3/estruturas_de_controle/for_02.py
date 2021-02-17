#!/usr/bin/python3


# Exepmplo com string
palavra = 'paralelepípedo'

for letra in palavra:
    print(letra)

for letra in palavra:
    print(letra, end=',')
print('Fim!')

# Exepmplo com lista
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']

for nome in aprovados:
    print(f'O aluno {nome} foi aprovado!')

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

# Exepmplo com tupla

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', "Sábado")

for dia in dias_semana:
    print(f'Hoje é {dia}')
