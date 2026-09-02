"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

def validar_digito01cpf(cpf):
    nove_digits = cpf[:9]

    conta_digits = 0
    contador01 = 10
    for digito in nove_digits:
        conta_digits += contador01 * int(digito)
        contador01 -= 1

    conta_final = (10 * conta_digits) % 11

    if conta_final > 9:
        digito_01 = '0'
    else:
        digito_01 = str(conta_final)

    return digito_01

print(validar_digito01cpf('36536516621')) # Validado
print(validar_digito01cpf('85932200880')) # Validado
print(validar_digito01cpf('16772962591')) # Validad