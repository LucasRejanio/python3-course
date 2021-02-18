#!/usr/bin/python3


# While infinito
def fibonacci():
    penultimo = 0
    ultimo = 1

    print(f'penultimo {penultimo} e ultimo {ultimo}')

    while True:
        proximo = penultimo + ultimo
        print(f'proximo: {proximo}')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
