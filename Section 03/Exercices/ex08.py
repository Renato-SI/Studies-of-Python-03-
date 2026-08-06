"""
Crie um programa que receba uma frase e exiba qual letra apareceu
mais vezes, ignorando os espaços. Em caso de empate, considere
a primeira letra encontrada.
"""

frase = "A tecnologia transforma o mundo e a programacao permite criar soluçoes para desafios do dia a dia"

i = 0
qtd_ltr_apareceu_mais = 0
letra_que_apareceu_mais = ''

while i < len(frase):

    ltr_atual = frase[i]

    if ltr_atual == ' ':
        i += 1
        continue

    # Contando quantas vezes a letra que corresponde ao i atual aparece na frase.
    qtd_ltr_atual = frase.lower().count(ltr_atual)

    # Se a Letra atual apareceu mais vezes que a letra de maior quantidade anterior
    # A Váriavel de qtd e da letra são atualizadas, a condição abaixo é checada em cada Loop.
    if qtd_ltr_apareceu_mais < qtd_ltr_atual:
        qtd_ltr_apareceu_mais = qtd_ltr_atual
        letra_que_apareceu_mais = ltr_atual

    i += 1

# Print fora do Loop para exibir apenas a quantidade e qual letra apareceu mais ao final de tudo.
# Caso o print Fosse colocado dentro do Loop ele exibiria qual letra apareceu mais e sua qtd a cada volta do LOOP. 
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais}", ela apareceu '
    f'{qtd_ltr_apareceu_mais}x vezes'
)