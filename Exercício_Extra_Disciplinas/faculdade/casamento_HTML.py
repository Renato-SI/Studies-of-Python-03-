"""
Crie uma função que receba uma string contendo tags HTML e verifique se todas as tags estão corretamente ab ertas e fechadas.
Utilize uma pilha (stack) para controlar as tags abertas. Sempre que uma tag de abertura for encontrada, ela deve ser adicionada à pilha.
Quando uma tag de fechamento for encontrada, ela deve corresponder à tag que está no topo da pilha.
A função deve retornar True caso todas as tags estejam corretamente fechadas e False caso exista algum a tag sem fechamento, 
uma tag fechada fora de ordem ou uma tag de fechamento sem uma abertura correspondente.
Saída esperada:
'<div<p>Texto</p></div>' = False
'</div>' =  False
'<html><body><h1>Hello</h1></body></html>' = True
'<div><p>Olá</p></div>' = True
"""

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