"""
Faça um programa que peça ao usuário um número inteiro positivo.
Utilizando while, faça uma contagem regressiva começando pelo número informado e terminando em 0.
"""

numero = int(input("Digite um número inteiro positivo: "))

while numero >= 0:
    print(numero)
    numero -= 1