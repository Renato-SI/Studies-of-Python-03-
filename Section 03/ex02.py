#Exercício referente à aula 49.

name = input("Digite seu Nome: ").strip()
age = input("Qual sua idade? ").strip()

if name and age:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")

    if " " in name:
        print(f"Seu nome contém {name.count(" ")} espaços")
    else:
        print("Seu nome não contém espaços!")
        
    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[-1]}")
else:
    print("Desculpe, voce deixou campos vazios.")