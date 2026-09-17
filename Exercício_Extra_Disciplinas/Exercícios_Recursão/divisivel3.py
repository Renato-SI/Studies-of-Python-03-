""" 
Crie uma função que receba um número inteiro e retorne a soma de todos os seus dígitos. 
O cálculo deve ser realizado utilizando um loop. 
O dígito 0 deve ser ignorado durante a soma. 
Exemplos: 123 -> 6 105 -> 6 1000 -> 1 178 -> 16 
"""

def divisivel3(num:int):
    if num == 3 or num == 6 or num == 9:
        return True
    elif num < 12:
        return False
    digits_sum = sum(int(digit) for digit in str(num))
    return divisivel3(digits_sum)


print(divisivel3(1000))
print(divisivel3(91))
print(divisivel3(178))
print(divisivel3(19))
print(divisivel3(13))
print(divisivel3(1))