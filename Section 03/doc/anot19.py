# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Renato', 'Anna nery', 1, 2, 3, 'Rodrigues']
tupla = 'Python', 'é', 'Prático'
salas = [
    # 0        1
    ['gta5', 'renato', ],  # 0
    # 0
    ['gow5', ],  # 1
    # 0       1       2
    ['gow4', 'jane', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')