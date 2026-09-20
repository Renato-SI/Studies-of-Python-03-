def verificar_ocorrencia(lista:list, valor):
    if len(lista) == 0 :
        return 0
     
    if lista[0] == valor:
        return 1 + verificar_ocorrencia(lista[1:], valor)
    
    return verificar_ocorrencia(lista[1:], valor)

l = ['a', 'b', 'c', 'a', 'a']

print(verificar_ocorrencia(l, 'a')) # 3