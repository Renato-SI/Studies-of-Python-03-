#Exercício Simples da Aula 40, Objetivo é apenas mostrar qual valor é maior sem conversão para int.

primeiro_valor = input("Digite o Primeiro Valor: ")
segundo_valor = input("Digite o Segundo Valor: ")

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é  maior do que {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior do que {primeiro_valor=}")
elif primeiro_valor == segundo_valor:
    print(f"Os Valores {primeiro_valor} & {segundo_valor} são iguais.")