"""
Faça um programa que peça ao usuário um número inteiro positivo.
Depois, utilizando while, mostre na tela todos os números de 1 até o número informado.
Essa é uma Versão que trabalha conceitos gerais para validar as entradas do user
/ Aprimoramento do Ex09.py
"""
# Fiz essa Versão com algumas Válidações Básicas, a ultima parte está sem validações
# O sistema apenas vai acet
while True:

    numero = input("Digite um número inteiro + : ")

    try:
        numero = int(numero)

        if numero <= 0:
            print("Digite um Número Inteiro Positivo maior que 0")
            continue

    except:
        print("Tente Digitar um Número Inteiro Positivo!!")
        continue

    i = 1
    # Parte Central do Exercício, no qual faz a contagem
    while i <= numero:

        print(i)
        i += 1

    user_choice = input(
        "Deseja escolher outro Número? [S] ou [N] pra sair: "
    ).lower()

    # Válida se o usuário digitou Não, caso sim, ele sai do PROGRAMA!
    # Aqui eu utilizei o startswith pra facilitar a vida do usuario.
    # Porém existem melhores opções, para programas mais complexos, esta é uma simples aplicação do exercicio ofertado.
    if user_choice.startswith("n"):
        print("Foi Ótimo te-lo conosco!")
        break