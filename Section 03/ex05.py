"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver 5 e 6 letras, escreva "Seu nome é normal". Maior que 6 escreva "Seu nome é muito grande".
"""

name = input("Digite seu Primeiro Nome: ").strip()
check_name = name.replace(" ", "").isalpha() #Vai remover os espaços entre nomes e checar se contém apenas letras!
len_name = len(name)

# O check_name com o replace poderia ser usado em casos de o usuário digitar seu nome Coompleto!
# Utilizei ele apenas para testar o funcionamento do isalpha (Só Válida letras, espaços ele retorna False)

if check_name and (len_name > 1):
    if len_name <= 4: 
        print("Seu nome é Curto!")
    elif 4 < len_name <= 6:
        print("Seu nome é normal!")
    else:
        print("Seu nome é Grande!")
else:
    print("Tente Inserir mais de 01 Letra\nVerifique se contém apenas Letras.")