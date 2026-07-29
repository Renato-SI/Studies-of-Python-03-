"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
#pontos = 0

#while pontos < 10:
#    pontos = pontos + 1
#    print(pontos)

#print('Acabou')

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
contador = 10

while contador >= 0:
    
    if contador % 2 == 0:
        print(f"{contador} é Par")
    else:
        print(f"{contador} é Ímpar")

    contador -= 1

print("------FIM------")