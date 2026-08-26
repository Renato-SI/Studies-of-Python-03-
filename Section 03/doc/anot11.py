"""
Tudo que utilizamos dentro de um While pode ser utilizado dentro de um for!
Seguindo o mesmo raciocínio, só que agr não é necessário ficar iterando.
"""

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')