def divisivel8(numero, k=0):
    if k * 8 == numero:
        return True
    elif k * 8 > numero:
        return False
    else:
        return divisivel8(numero, k + 1)

entrada = int(input(''))
print(divisivel8(entrada))