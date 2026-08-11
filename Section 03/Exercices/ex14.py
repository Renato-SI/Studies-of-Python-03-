"""
Crie um programa que tenha uma senha definida diretamente no código.

O programa deve pedir ao usuário que informe a senha. Enquanto a senha estiver incorreta, o programa deve continuar pedindo novamente.

Quando o usuário acertar, mostre: Acesso permitido
"""
while True:

    PASSWORD = "12345"
    user_choice = input("Digite sua Senha: ")

    if user_choice == PASSWORD:
        print("Acesso Permitido!")
        break
    else:
        print("Senha Incorreta! Tente Novamente")