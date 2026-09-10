def casamento_perfeito(entrada):
    res = []

    for caracter in entrada:
        if caracter in '([{':
            res.append(caracter)

        elif caracter in ')]}':
            if len(res) == 0:
                return False
            
            topo = res.pop()

            if (topo == '(' and caracter != ')') or (topo == '[' and caracter != ']') or (topo == '{' and caracter != '}'):
                return False
             
    if len(res) == 0:
        return True
    
    return False

entrada = input("")
if casamento_perfeito(entrada):
    print('casamento perfeito')
else:
    print('casamento imperfeito')