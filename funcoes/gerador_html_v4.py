#!/usr/bin/python3


def tag_bloco(conteudo, *args, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*items):
    lista = ''.join((f'<li>{item}</li>' for item in items))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('Incluiído com sucesso', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(classe='error', conteudo='falhou'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))
