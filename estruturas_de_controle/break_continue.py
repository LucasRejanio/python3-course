#!/usr/bin/python3
from random import randint


# For com else
for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim!')


def sortear_dado():
     return randint(1, 7)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    if sortear_dado() == i:
        print(f'ACERTOU! O numero {i} é igual ao numero sorteado')
        break
else:
    print('Não acertou o número!')
