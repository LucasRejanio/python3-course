# Dicionário

pessoa = {
    'nome': 'Prof(a). Ana',
    'idade': 38,
    'cursos': [
        'Inglês',
        'Português'
    ]
}

# Acessando os valores do dicionário
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][1])

# Pegando as chaves do dicionário
print(pessoa.keys())

# Pegando os valores 
print(pessoa.values())
print(pessoa.get('idade'))

# Pegando chave e valor do dicionário
print(pessoa.items())

segunda_pessoa = {
    'nome': 'Prof. Alberto',
    'idade': 43,
    'cursos': [
        'React',
        'Python'
    ]
}

# modificando valores do dicionário
segunda_pessoa['idade'] = 44
segunda_pessoa['cursos'].append('Angular')
print(segunda_pessoa)

# Lendo e removendo valor do dicionário
segunda_pessoa.pop('idade')
del segunda_pessoa['cursos']

# Update no dicionário 
segunda_pessoa.update({'idade': 40, 'sexo': 'Masculino'})

# Limpar todo o dicionário
segunda_pessoa.clear()
