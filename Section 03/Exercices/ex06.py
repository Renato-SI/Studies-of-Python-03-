"""
Iterando strings com While; aula 65
"""
# Exemplo do Funcionamneto
name = "Renato Rodrigues"
new_name = "*"
index = 0

while index < len(name):

    # Para cada Index da str guardada na variavel name, vai ser Adicionado um * ao final do nome!
    # Assim "Fatiando" a string e depopis reconpondo ela, ao final de 01 volta o index atualiza para + 1!
    new_name += f"{name[index]}*"
    index += 1 

print(new_name)
