""" while/else """
# Conceito aparentemente pouco utilizado, Abordado na Aula 70

string = 'Renato Rodrigues Filho'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break # Se colocar um continue, nunca iremos sair do Loop, já que ele vai ficar sempre preso no index do " " e sem atualizar o i += 1.

    print(letra)
    i += 1

# O else só vai rodar quando o Bloco de Código do While for completamente executado
# Como neste caso temos um "Break" quando o indice da str corresponder a um " ", logo o else não é executado!
else:
    print('Não encontrei um espaço na string.')
    
print('Fora do while.')