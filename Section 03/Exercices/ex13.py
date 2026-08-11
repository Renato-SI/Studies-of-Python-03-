"""
Faça um programa que peça ao usuário um número inteiro. 
Depois, utilizando while, mostre a tabuada desse número de 1 até 10.
"""

tabuada = int(input("Deseja visualizar a Tabuada de Qual Número? "))

i = 1

while i <= 10:
    print(f"- {tabuada} X {i} = {tabuada * i}")
    i += 1