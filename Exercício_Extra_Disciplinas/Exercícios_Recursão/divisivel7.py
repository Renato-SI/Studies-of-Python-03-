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
    
    last_digit = numero % 10
    remaining_digits = numero // 10
    new_number = (last_digit * 5) + remaining_digits
    return divisivel7(new_number)
    

def tempo(n):
    import time
    start = time.time()
    result = divisivel7(n)
    end = time.time()
    return f"A função divisivel7({n})= {result}, rodou em: {end - start:.10f}"

print(tempo(1000213123010321212121212172816261638136183131))