"""
Desenvolva um programa em Python 3 que leia um pseudocódigo iniciado por INICIO e finalizado por FIM, calculando seu tempo total de execução.

As instruções possuem os seguintes custos:

IO → 30 unidades
MEM → 10 unidades
PROCSUM → 1 unidade
PROCMULT → 10 unidades

Os comandos LOOP X ... FIMLOOP repetem o bloco interno X vezes. Podem existir loops aninhados em até 2 níveis de profundidade.

Sempre que um loop for fechado, o custo acumulado dentro dele deve ser multiplicado pela quantidade de repetições e incorporado ao custo total.

A entrada será fornecida em uma única linha, podendo conter espaços, tabulações e quebras de linha, que devem ser ignorados.

A saída deve apresentar apenas o tempo total de execução, como um número inteiro.
"""

import sys

entrada = sys.stdin.read()
entrada = entrada.split()

custos = {
    "IO": 30,
    "MEM": 10,
    "PROCSUM": 1,
    "PROCMULT": 10
}

repeticoes = []
custos_loop = []
total = 0

for i in range(len(entrada)):

    comando = entrada[i]

    if comando == "LOOP":
        vezes = int(entrada[i + 1])
        repeticoes.append(vezes)
        custos_loop.append(0)

    elif comando == "FIMLOOP":
        vezes = repeticoes.pop()
        custo = custos_loop.pop()
        custo *= vezes

        if custos_loop:
            custos_loop[-1] += custo
        else:
            total += custo

    elif comando in custos:
        if custos_loop:
            custos_loop[-1] += custos[comando]
        else:
            total += custos[comando]

print(total)