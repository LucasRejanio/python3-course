#!/usr/bin/python3

# [expressão for item in list if condicional]
dobros_pares = [i * 2 for i in range(1, 10) if i % 2 == 0]
print(dobros_pares)

# Versão "normal"
dobros_pares = []

for i in range(1, 10):
    if i % 2 == 0:
        dobros_pares.append(i * 2)
print(dobros_pares)
