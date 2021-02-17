#!/usr/bin/python3

# Constant
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'A plavra {palavra} é proibida no nosso aplicativo')
            break
    else:
        print('Texto autorizado:', texto)
