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

def validar_cpf(cpf_user):
    nove_digits = cpf_user[:9]

    conta_digits = 0
    contador01 = 10
    for digito in nove_digits:
        conta_digits += contador01 * int(digito)
        contador01 -= 1

    conta_final = (10 * conta_digits) % 11

    if conta_final > 9:
        digito_01 = 0
    else:
        digito_01 = conta_final

    dez_digits = nove_digits + str(digito_01)

    conta_digits02 = 0
    contador02 = 11
    for digit in dez_digits:
        conta_digits02 += contador02 * int(digit)
        contador02 -= 1

    conta_final02 = (10 * conta_digits02) % 11

    if conta_final02 > 9:
        digito_02 = 0
    else:
        digito_02 = conta_final02

    cpf_calculado = f'{nove_digits}{digito_01}{digito_02}'
    if cpf_user == cpf_calculado:
        return f'O CPF: {cpf_user} é Válido'

    else:
        return f'O CPF: {cpf_user} não é Válido'
    
print(validar_cpf('47869994820'))  #Validado
print(validar_cpf('48530330765'))  #Validado
print(validar_cpf('86819936664'))  #Validado
print(validar_cpf('54259728148'))  #Validado