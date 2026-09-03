"""
INSTRUÇÕES DA ATIVIDADE DE CÍCERO (Colisões / 12/08)
Escreva um programa que, dados dois retângulos, determine se eles se interceptam ou não.

Entrada:
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). 
Cada caso de teste contém duas linhas. Cada linha contém quatro inteiros:
x0, y0, x1, y1, sendo 0 ≤ x0 < x1 ≤ 1.000.000 e 0 ≤ y0 < y1 ≤ 1.000.000,
separados por um espaço em branco representando um retângulo.
Os lados do retângulo são sempre paralelos aos eixos x e y.

Saída:
Seu programa deve imprimir, na saída padrão, uma única linha para cada caso de teste,
contendo o número 0 (zero) caso não haja interseção ou o número 1 (um) caso haja.

Entradas e Saídas esperadas do Programa:
- Entrada: 0 0 1 1 0 0 1 1 & Saída: 1
- Entrada: 0 0 2 2 1 1 3 3 & Saída: 1
- Entrada: 0 0 1 1 2 2 3 3 & Saída: 0
- Entrada: 1 2 4 5 2 3 5 1 & Saída: 1
"""
entrada = input().split(" ")
valores_int = [] 

for valor in entrada:
    valores_int.append(int(valor))

x0_a = min(valores_int[0], valores_int[2])
x1_a = max(valores_int[0], valores_int[2])
y0_a = min(valores_int[1], valores_int[3])
y1_a = max(valores_int[1], valores_int[3])

x0_b = min(valores_int[4], valores_int[6])
x1_b = max(valores_int[4], valores_int[6])
y0_b = min(valores_int[5], valores_int[7])
y1_b = max(valores_int[5], valores_int[7])

"""
Fiz algumas anotações no caderno e concluí que era mais fácil verificar quando Não ocorre as colisões
já que só existem 04 casos que a colisão não ocorre:
Basicamente Desenhei no caderno

Casos do X:
- Retangulo_A na esquerda do B: x1_a < x0_b
- Retangulo_A na direita do B: x0_a > x1_b

Casos do Y:
- Retangulo_A acima do B: y0_a > y1_b
- Retangulo_A abaixo do B: y1_b < y0_b
"""

nao_colide_x_y = (
    x1_a < x0_b or
    x0_a > x1_b or
    y0_a > y1_b or
    y1_a < y0_b
)

if nao_colide_x_y:
    print(0)
else:
    print(1)