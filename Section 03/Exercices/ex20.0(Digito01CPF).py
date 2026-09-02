"""
Calcula os dois dígitos verificadores de um CPF.

O primeiro dígito é calculado a partir dos 9 primeiros números,
multiplicados por uma contagem regressiva de 10 a 2.

O segundo dígito utiliza os 9 primeiros números mais o primeiro
dígito, multiplicados por uma contagem regressiva de 11 a 2.

Em ambos os casos, a soma é multiplicada por 10 e o resto da
divisão por 11 determina o dígito verificador. Caso o resultado
seja maior que 9, o dígito será 0.
"""

def validar_cpf(cpf_user):
    # PARTE DO DÍGITO 01
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

    # PARTE DO DÍGITO 02
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

    # VALIDAR O CPF FORMADO
    cpf_calculado = f'{nove_digits}{digito_01}{digito_02}'

    if cpf_user == cpf_calculado:
        return (
            f'O CPF: {cpf_user[:3]}.{cpf_user[3:6]}.'
            f'{cpf_user[6:9]}-{digito_01}{digito_02} é Válido')

    else:
        return (
            f'O CPF: {cpf_user[:3]}.{cpf_user[3:6]}.'
            f'{cpf_user[6:9]}-{digito_01}{digito_02} não é Válido')
    
print(validar_cpf(
    '478.699.948-20'.replace('-', '').replace('.', '')
    )) 
print(validar_cpf(
    '485.303.307-65'.replace('-', '').replace('.', '')
    ))  
print(validar_cpf(
    '868.199.366-64'.replace('-', '').replace('.', '')
    ))
print(validar_cpf(
    '54259728148'.replace('-', '').replace('.', '')
    ))  