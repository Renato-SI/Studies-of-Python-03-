def hanoi_tower(n_discos, origem='A', destino='C', auxiliar='B'):
    if n_discos == 1:
        print(f'O Disco 1 deve ser movido da torre {origem} para {destino}')
    elif n_discos > 1:
        hanoi_tower(n_discos - 1, origem, auxiliar, destino)
        print(f'O Disco {n_discos} deve ser movido da torre {origem} para {destino}')
        hanoi_tower(n_discos - 1, auxiliar, destino, origem)

hanoi_tower(5)