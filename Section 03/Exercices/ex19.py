"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
def clear():
    os.system('cls')

lista = []
while True:
    print('====== SELECIONE UMA OPÇÃO ======')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [n]air: ').lower().strip()

    if opcao == 'i':
        clear()
        item = input('Nome do item: ').capitalize().strip()
        lista.append(item)

    elif opcao == 'a':
        apagar_item = input('Escolha o índice para apagar: ').strip()

        try: 
            indice = int(apagar_item)
            del lista[indice]

        except ValueError:
            print('Por favor digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        clear()
            
        if len(lista) == 0:
            print('Não Há itens para se listar!')
            continue

        print('===== LISTA DE COMPRAS =====')
        for itens in range(len(lista)):
            print(itens, lista[itens])

    elif opcao.startswith('n'):
        break

    else:
        print('Escolha entre: i, a, l, n')