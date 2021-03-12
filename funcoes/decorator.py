#!/usr/bin/python3


def log(funcao):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da função: {funcao.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = funcao(*args, **kwargs)
        print(f'resultado: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    soma(5, 7)
    sub(5, 7)
