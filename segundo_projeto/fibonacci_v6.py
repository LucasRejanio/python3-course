#!/usr/bin/python3


# Usando quantidade
def fibonacci(quantidade):
    resultado = [0, 1]

    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequencia
    for fib in fibonacci(20):
        print(fib)
