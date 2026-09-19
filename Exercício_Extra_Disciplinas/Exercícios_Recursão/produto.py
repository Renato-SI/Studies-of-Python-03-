def multiplicar(a,b):
    if a < b:
        return multiplicar(b,a)
    if a == 0 or b == 0:
        return 0 
    else:
        return a + multiplicar(a, b - 1)