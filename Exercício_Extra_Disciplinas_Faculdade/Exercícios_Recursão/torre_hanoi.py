"""
Cria uma função recursiva para resolver a Torre de Hanói.

A função deve calcular a quantidade mínima de movimentos necessários
para mover uma quantidade determinada de discos de uma haste para outra,
seguindo as regras da Torre de Hanói.

Para cada novo disco adicionado, a quantidade de movimentos é calculada
a partir da solução dos discos anteriores, seguindo a lógica recursiva.
"""

def hanoi(n):
    if n == 1:
        return 1
    elif n > 1:
        return (2 ** n) - 1
    else:
        return 'Digite um Número inteiro positivo'

print(hanoi(1))
print(hanoi(4))
print(hanoi(5))
print(hanoi(6))