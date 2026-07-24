"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropiada.
Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

entrada = (input("Que Horas são? ex: 10:59: "))
try:
    time = int(entrada)

    if time >= 0 and time <= 11:
        print("Bom dia!")
    elif time >= 12 and time <= 17:
        print("Boa tarde!")
    elif time >= 18 and time <= 23:
        print("Boa noite!")
    else:
        print("Não conheço essa hora")

except:
    print("Por favorm digite apenas números inteiros.")