#!/usr/bin/python3


# Usando for ao invés do while
def fibonacci(quantidade):
    resultado = [0, 1]

    # A variavel "_" não está sendo usada
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequencia
    for fib in fibonacci(20):
        print(fib)
