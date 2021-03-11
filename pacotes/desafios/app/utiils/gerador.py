# Choice seleciona um valor aleatorio
from random import choice


nomes = ['Ana', 'Maria', 'Pedro', 'Rafael']


def novo_nome():
    return choice(nomes)
