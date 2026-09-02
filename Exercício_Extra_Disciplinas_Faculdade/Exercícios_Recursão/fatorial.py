"""
Crie uma função recursiva chamada fatorial(n) que calcule
o fatorial de um número inteiro n.

O fatorial de n é dado por:
n! = n * (n - 1) * ... * 1
"""

def fat(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * fat(n - 1)
    else:
        return "Erro!"
print(fat(10))   

# OU

def fat_02(n):

    if n > 1:        
        i = 1
        for j in range(1, n + 1):
            i *= j 
        return i 
    else:
        return "Erro!"
print(fat_02(10))