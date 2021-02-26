# Curso python3

Esse repositorio tem como objetivo armazenar todo o material desenvolvido no curso de python3 ministrado pela empresa cod3r. 

- Linkd do curso: https://www.udemy.com/course/curso-python-3-completo/

## Tipos
Python é uma linguagem de tipos dinâmicos, ou seja, não é necessário fazer casting como em Java, Pascal ou C.

O conceito de variável é uma associação entre um nome e um valor, mas não é necessário declarar o tipo da variável, portanto, o tipo relacionado à variável pode variar durante a execução do programa, o que implica em muitos aspectos o uso da linguagem.

Existem 4 tipos numéricos:

- inteiro (int)
- ponto flutuante (float)
- booleano (bool) **pode ser 0 e 1 ou False e True**
- complexo (complex)
- Suportam adição, subtração, multiplicação e divisão e também podem se relacionar.

Existe também o seguinte tipo:

string (str)

## Operadores matemáticos
O Python pode ser utilizado como uma calculadora matemática avançada. Praticamente, todos os operadores aritméticos funcionam da mesma forma como os conhecemos da matemática elementar. Por exemplo, para trabalharmos com as 4 principais funções matemáticas, a soma, subtração, multiplicação e divisão, temos os operadores conforme tabela a seguir.

| Operação	| Operador |
|-----------|----------|
| adição    | + |
| subtração	| - |
| multiplicação	| * |
| divisão   |	/ |

## Dicionário
Dicionário é um tipo diferente de coleção. Ele é um tipo de mapeamento nativo do Python. Um mapa é uma coleção associativa desordenada. A associação, ou mapeamento, é feita a partir de uma chave, que pode ser qualquer tipo imutável, para um valor, que pode ser qualquer objeto de dados do Python.

## Lista 
Em Python, uma lista é representada como uma sequência de objetos separados por vírgula e dentro de colchetes [], assim, uma lista vazia, por exemplo, pode ser representada por colchetes sem nenhum conteúdo.

## Tupla 
Tupla é uma Lista imutável. O que diferencia a Estrutura de Dados Lista da Estrutura de Dados Tupla é que a primeira pode ter elementos adicionados a qualquer momento, enquanto que a segunda estrutura, após definida, não permite a adição ou remoção de elementos.

## Operadores lógicos
Há três operadores lógicos: and, or e not. A semântica (significado) destes operadores é semelhante ao seu significado em inglês. Por exemplo, x > 0 and x < 10 só é verdade se x for maior que 0 e menor que 10.

### Tabela verdade

#### Tabela Verdade: Operador AND

|A     |              | B     |          | and (A +B)|
|------|--------------|-------|----------|-------|
|True  |              | True  |          | True |
|True  |              | False |          | False |
|False |              | True  |          | False |
|False |              | False |          | False |

#### Tabela Verdade: Operador OR

|A     |              | B     |          | OR (A + B)|
|------|--------------|-------|----------|-------|
|True  |              | True  |          | True |
|True  |              | False |          | True |
|False |              | True  |          | True |
|False |              | False |          | False |

#### Tabela Verdade: Operador XOR 

|A     |              | B     |          | != (A + B)|
|------|--------------|-------|----------|-------|
|True  |              | True  |          | False |
|True  |              | False |          | True |
|False |              | True  |          | True |
|False |              | False |          | False |

#### Tabela Verdade: Operador NOT 

|A     |              | NOT ( ~A) |    
|------|--------------|-----------|
|True  |              | False|        
|False |              | True |      


## if e else
Quando programamos, muitas vezes precisamos que determinado bloco de código seja executado apenas se uma determinada condição for verdadeira. Em casos assim, devemos fazer uso de uma estrutura de condição.

Neste documento você aprenderá a utilizar a estrutura de condição if-else e elif em Python.

Sintaxe da instrução if do Python:

```py
idade = 18
if idade < 12:
    print('crianca')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')
```

# Estrutura de repetição
As estruturas de repetição são utilizadas quando queremos que um bloco de código seja executado várias vezes.

Em Python existem duas formas de criar uma estrutura de repetição:

- O for é usado quando se quer iterar sobre um bloco de código um número determinado de vezes.

- O while é usado quando queremos que o bloco de código seja repetido até que uma condição seja satisfeita. Ou seja, é necessário que uma expressão boleana dada seja verdadeira. Assim que ela se tornar falsa, o while para.

## while
O Laço de Repetição while repete um bloco de instrução enquanto a condição definida em seu cabeçalho for verdadeiro.

A estrutura while talvez seja a mais simples para entendermos nesse momento, porém, não raramente encontramos alunos que dizem não entender o funcionamento dessa estrutura. Se você entendeu o funcionamento da estrutura if, pense na estrutura while como sendo a estrutra if mas que ao invés de executar o seu bloco de instrução uma única vez, executará enquanto a expressão definida for igual a True.

O que diferencia o if do while é só e somente só a quantidade de vezes que o seu bloco de instrução será executado!

Exemplo: 

```py
conta = 0
while(conta <= 10):
    conta += 1
    print(conta)
```

## For
O laço for nos permite percorrer os itens de uma coleção e, para cada um deles, executar o bloco de código declarado no loop.

```py
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
```
É possível adicionar a instrução else ao final do for. Isso faz com que um bloco de código seja executado ao final da iteração, como mostra o exemplo a seguir:

```py
nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")
```

## Função
Em Python, uma função é uma sequência de comandos que executa alguma tarefa e que tem um nome. A sua principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos uma solução do problema.

#### Tipos de parametro
- **Posicional:** Parametros já esperados pela função sendo atribuidos por argumentos ordenados. 

- **Nomeado:** Parametros já esperados pela função sendo atribuidos por argumentos orientados(fora de ordem). 

Exemplo: 

```py
def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == '__main__':
    ## Posicional
    print(tag_bloco('Incluiído com sucesso', 'info', True,))
    # Nomeado
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(classe='error', texto='falhou'))
```
