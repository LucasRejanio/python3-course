#!/usr/bin/python3


# Alterando variavel
def fibonacci(limite):
    penultimo = 0
    ultimo = 1

    while ultimo < limite:
        print(f'penultimo {penultimo} e ultimo {ultimo}')
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(f'proximo: {ultimo}')


if __name__ == '__main__':
    fibonacci(1000)
