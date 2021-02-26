#!/usr/bin/python3


def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    print(tag_bloco('Incluiído com sucesso', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(classe='error', texto='falhou'))
