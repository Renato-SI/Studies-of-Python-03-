"""
Crie uma função recursiva chamada divisivel7(numero) para verificar
se um número é divisível por 7 utilizando a regra:

Pegue o último dígito, multiplique por 5 e some à parte restante
do número. Repita o processo recursivamente até determinar se o
número é divisível por 7.

Entrada:
    Um número inteiro maior que zero.

Saída:
    "s" se for divisível por 7 ou "n" caso contrário.

Restrições:
    - Usar recursão.
    - Não utilizar for, while, listas ou dicionários.
    - Não utilizar funções prontas para calcular a divisibilidade.
"""

entrada = int(input(""))

def divisivel7(numero):
    if numero == 7 or numero == 49:
        return "s"
    elif numero < 14:
        return "n"
    else: 
        last_digit = numero % 10
        remaining_digits = numero // 10
        mulandsum = (last_digit * 5) + remaining_digits
        return divisivel7(mulandsum)
    
print(divisivel7(entrada))