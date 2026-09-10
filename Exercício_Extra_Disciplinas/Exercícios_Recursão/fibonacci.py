"""
Crie uma função recursiva chamada fibonacci(n) que retorne
o n-ésimo termo da sequência de Fibonacci.

A sequência começa com 0 e 1, onde cada termo é a soma dos
dois anteriores.
"""

def fibonacci(n):
    # Caso Base
    if n >=1 and n <= 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    else: 
        return "Apenas positivos!"
#print(fibonacci(100)) -> lento   

# Uma forma mais rápida de se satisfazer o problema nesse caso é com iterações
# Se usar o catch a forma de cima é muito rápida também, quase instantânea
def fibiter(n):
    # Caso Base novamente
    if n >= 1 and n <= 2:
        return 1
    elif n > 2:
        ultimo = 0
        penultimo = 1
        for i in range(1, n+ 1):
            proximo = ultimo + penultimo
            penultimo = ultimo
            ultimo = proximo
        return proximo
    else:
        return "Erro! n deve ser maior que 0"

print(fibiter(100)) # -> Rápido