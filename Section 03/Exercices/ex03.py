"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

entrada = input("Digite um Número Inteiro: ")
try:
    number = int(entrada)
    if number % 2 == 0:
        print(f"O número {number} é Par!")
    else:
        print(f"O número {number} é Ímpar!")

except:
    print("Você não digitou um número inteiro")