"""
Crie uma lista de compras e permita ao usuário informar
alimentos que estão inaptos para consumo. Remova esses
alimentos da lista e exiba a lista atualizada com seus índices.
"""

inapto = []
lista = ['Feijão', 'Morango', 'Cenoura', 'Tomate', 'Cebola']

while True:
    adicionar = input('Existe algum alimento inapto ao consumo em sua casa? ').lower()

    if adicionar.startswith('n'):
        break

    adicionar_elemnto = input('Digite qual alimento está inapto: ').capitalize()
    inapto.append(adicionar_elemnto)

lista.append('Margarina')

for n in inapto:
    if n in lista:
        lista.remove(n)

print("===== Lista de Compras =====")

for index in range(len(lista)):
    print(index, lista[index])