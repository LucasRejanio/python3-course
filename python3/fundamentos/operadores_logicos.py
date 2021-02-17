# Operadoresa lógicos

print(True or False)
print(7 != 3 and 2 > 3)

# Tabela verdade do AND
print('Tabela verdade do AND')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabela verdade do OR
print('Tabela verdade do OR')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Tabela verdade do XOR (ou exclusivo)
print('Tabela verdade do XOR (ou exclusivo)')
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Operador de Negação (unário)
print('operador de Negação (unário)')
print(not True)
print(not False)
print(not 0)
print(not 1)

# Operadores Bit a Bit
print('Operadores Bit a Bit')
print(True & False)
print(False | True)
print(True ^ False)

# Um pouco da realidade
print('Um pouco da realidade!')
saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
print(meta)
