"""
Faça um programa que peça ao usuário um número inteiro positivo.
Depois, utilizando while, mostre na tela todos os números de 1 até o número informado.
"""

# Versão Simples do Exercício.

numero = int(input("Digite um número inteiro positivo: "))

i = 1

while i <= numero:
    print(i)
    i += 1