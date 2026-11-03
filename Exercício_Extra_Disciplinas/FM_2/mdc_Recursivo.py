def mdc(a, b):
    """
    Calcula o MDC de forma recursiva.
    Complexidade do algoritmo: O(log n)
    """
    if a < b:
        return mdc(b, a)
    if b == 0:
        return a
    
    # O AmodB (%) Garante que o maior multiplo do Menor valor esteja sendo utilizado, assim funcionaria como:
    # Retornar o Menor == B & B - Multiplo do Maior (A). O mod permite justamente pegar o resto da divisão do a pelo b
    # Ou seja, é como se eu pegasse o maior multiplo de B que cabe em A e subtraísse A por ele, assim obtendo o resto de forma eficiente.   
    return mdc(b, a % b) 

print(mdc(1024, 22))