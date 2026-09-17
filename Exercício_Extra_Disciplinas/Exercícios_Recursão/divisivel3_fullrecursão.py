""" 
Crie uma função recursiva que receba um número inteiro e retorne a soma de seus dígitos. O dígito 0 deve ser ignorado durante a soma. 
A função deve utilizar recursão para realizar o cálculo, 
sem utilizar laços de repetição ou converter o número para string. Exemplos: 123 -> 6 105 -> 6 1000 -> 1 
"""

def sum_digits(num):
    if num < 10:
        return num
    else: 
        return num % 10 + sum_digits(num//10)

def divisivel3(n):
    if n == 3 or n == 6 or n == 9:
        return True
    elif n < 12:
        return False
    else:
        somar_digitos = sum_digits(n)
        return divisivel3(somar_digitos)

print(divisivel3(69))
print(divisivel3(99))
print(divisivel3(21948))
print(divisivel3(19))
print(divisivel3(13))
print(divisivel3(1))