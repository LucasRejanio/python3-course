# Operadores ternários 

esta_chovendo = True

print('hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])
print('hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))

# Mais Operadores

# Operador de membro
lista = [1, 2, 3, 'Ana', 'Carla']

print(2 in lista)

print('Ana' not in lista)

# Operador de identidade
x = 3
y = x
z = 3
print(x is y)
print(x is not z)

# Operador de String
frase = 'Python é uma linguagem excelente'
print('py' not in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())
print(frase.split('e'))
