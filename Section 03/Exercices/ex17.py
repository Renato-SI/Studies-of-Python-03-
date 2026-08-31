"""
Exercício
Exiba os índices da lista
0 Renato
1 Anna Nery
2 Luciana
"""

lista = ['Renato', 'Anna Nery', 'Luciana']
# Se eu quiser mexer/ adicionar ou removger valores, nesse caso t5enho q fazer antes da variavel indice
# No caso Abaixo eu posso adicionar e remover sem me 'preocupar' com isso já que fiz da forma direta.
lista.append('Simba')
lista.append('Art')

# lista.pop
indice = range(len(lista))

print('=== METODO \'INDIRETO\' ===')
for index in indice:
    print(index, lista[index])

# OU de maneiraa direta!
print('=== METODO DIRETO ===')
for index in range(len(lista)):
    print(index, lista[index])