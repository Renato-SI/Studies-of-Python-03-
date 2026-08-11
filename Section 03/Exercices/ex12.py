"""
Faça um programa que peça ao usuário um número inteiro positivo. 
Utilizando while, mostre todos os números pares entre 0 e o número informado.
"""

numero = int(input("Digite um Número Inteiro Positivo: "))

i = 0
while i <= numero:
    print(i)
    # Basta percorrer o Próprio Indice de 02 em 02.
    # Como os Números Pares Iniciam em 0, essa opção é prática pois não necessita do if.
    i += 2

"""
Outras Maneiras a seguir:

Primeira: Conta na Ordem Decrescente
numero = int(input("Digite um Número Inteiro Positivo: "))

while numero >= 0:

    if numero % 2 == 0:
        print(numero)

    numero -= 1
-----------------------------------------------------------------------------------------
Segunda: Conta na ordem Crescente usando o If
numero = int(input("Digite um Número Inteiro Positivo: "))

i = 0
while i <= numero:

    if i % 2 == 0:
        print(i)
        
    i += 1
"""