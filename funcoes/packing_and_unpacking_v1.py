#!/usr/bin/python3


# Função com N parametos
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    # Exepmplo de packing
    print(soma_n(1,3,5,5,6,7,7))

    # Exemlo de unpacking
    tupla_nums = (1, 2, 3)
    print(soma_n(*tupla_nums))

    lista_nums = [1, 2, 3]
    print(soma_n(*lista_nums))
