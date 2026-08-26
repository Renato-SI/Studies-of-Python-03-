"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# Aqui daria pra mudar o Local do cls, mas ok!
import os

palavra_secreta = "manchester"
letras_acertadas = ""
tentativas = 0
while True:

    letra_digitada = input("Digite uma Letra: ").lower()
    
    if len(letra_digitada) > 1:
        print("Digite Apenas uma Letra!")
        continue
    os.system("cls")
    tentativas += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += "*"
    print(f"Palavra formada: {palavra_formada}")

    if palavra_formada == palavra_secreta:
        print(
            "Parabéns, você adivinhou!\n"
            f"A palavra era {palavra_secreta}!\n"
            f"O número de tentativas foi: {tentativas}X.")
        letras_acertadas = ""
        tentativas = 0
        break