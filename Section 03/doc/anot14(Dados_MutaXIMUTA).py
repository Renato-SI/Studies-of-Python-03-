"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# Quando uma variável aponta para outra que contém um tipo de dado mutável (lista_a)
# A variável B não vai fazer uma cópia de A e sim apontar para o mesmo valor na memoria, ou seja ela vai pegar alterações mesmo que sejam 
# posteriores, nesse caso abaixo, a lista_b vai ter o valor atualizado do index 0 da lista A, porque ambas as variaveis apontam para o mesmo local.
lista_b = lista_a

#lista_b = lista_a.copy(), fazendo assim , eu estaria criando de fato uma copia da lista a e agora estariam apontando para espaços diferentes na memoria.

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


"""
for in com listas
"""
# Mesmo funcionamento de percorrer uma variavel normal, so que agora cada index é uma palavra
# no geral os metodos de manipulação de str servem muito bem nas listas;
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))