"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    extend - estende a lista
    + - concatena listas
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
# o Método extend não retorna nada, então se fizessemos esta ação dentro de uma determinada variável
# e mandar um print na variavel, vai retornar None, o extend atua DIRETAMENTE NA LISTA SELECIONADA!
lista_a.extend(lista_b)
# O Print vai ser a junção daa lista a com a B pois o extend atuou diretamente na lista_a
print(lista_a)