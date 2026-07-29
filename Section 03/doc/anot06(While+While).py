"""
Repetições

while (enquanto)

Executa uma ação enquanto uma condição for verdadeira.

Loop infinito -> Quando um código não tem fim.
"""

# Utilizei a convenção da variável em CAPS, apenas para...
# Demonstrar que, nesse caso, os valores da QTD são fixos/constantes.

QTD_LINHAS = 5
QTD_COLUNAS = 5

linha = 1

while linha <= QTD_LINHAS:
    # Toda vez que o While acima rodar, a coluna recebe o valor 1.
    coluna = 1

    # O While Interno vai rodar 05 vezes para cada volta do While Externo!
    while coluna <= QTD_COLUNAS:
        print(f"linha={linha} & {coluna=}")
        coluna += 1

    linha += 1  # A quantidade de linhas só é atualizada após as 05 voltas do While Interno.

# OBS: A cada volta do While Interno ou Externo, sempre é necessário algo para "controlar" o número de loops.
# Neste caso, são 02 coisas: as estruturas atributivas (+=) e as restrições "obrigatórias" do próprio laço (coluna <= QTD_COLUNAS).

print("Acabou")