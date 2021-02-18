#!/usr/bin/python3


# While com limite
def fibonacci(limite):
    penultimo = 0
    ultimo = 1

    while ultimo < limite:
        print(f'penultimo {penultimo} e ultimo {ultimo}')
        proximo = penultimo + ultimo
        print(f'proximo: {proximo}')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(1000)
