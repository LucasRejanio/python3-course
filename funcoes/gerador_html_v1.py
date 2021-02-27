#!/usr/bin/python3


def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    print(f'Resultado:', tag_bloco('Incluiído com sucesso'))
