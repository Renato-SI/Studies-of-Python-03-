

def verificar_html(entrada):
    stack = []
    i = 0
    while i < len(entrada):
        if entrada[i] == '<':
            fim_tag = entrada.find('>', i)
            # n achou o final da tag que foi aberta
            if fim_tag == -1:
                return False
            # pego só o conteúdo interno da tag < ... >
            tag = entrada[i + 1: fim_tag]
            
            if tag[0] != '/':
                stack.append(tag)

            else:
                # Se a pilha estava vazia e ele achou uma abertura == False
                if not stack:
                    return False

                topo = stack.pop()
                # Se o topo da pilha for diferente da tag de fechamento que ele achou == False
                if topo != tag[1:]:
                    return False
                
            i = fim_tag

        i += 1

    return len(stack) == 0 

check_True = '<html><body><h1>Hello</h1></body></html>'
check_False = '<div<p>Texto</p></div>'

print(verificar_html(check_False))
print(verificar_html(check_True))