#!/usr/bin/python3


# Exepmplo com dicionario
produto = {
    'nome': 'Caneta chic',
    'preco': 14.99,
    'importada': True,
    'estoque': 793
    }

# Acessando chaves
for chave in produto.keys():
    print(chave)

# Acessando valores
for valor in produto.values():
    print(valor)

# Acessando chave e valor
for chave, valor in produto.items():
    print(f'chave {chave} valor {valor}')
