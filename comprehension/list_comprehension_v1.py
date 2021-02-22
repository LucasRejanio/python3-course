#!/usr/bin/python3

# [expressão for item in list]
dobros = [i * 2 for i in range(1, 10)]
print(dobros)

# Versão "normal"
dobros = []

for i in range(1, 10):
    dobros.append(i * 2)
print(dobros)
