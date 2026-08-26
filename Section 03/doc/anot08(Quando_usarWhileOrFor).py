"""
Quando Devo utilizar o While ou o for?

- A principal questão aqui é saber se o número de repetições é variado ou não, 
ou seja, saber se eu sei o fim de algo ou não!

Exemplo: Para Iterar sobre uma string

Com o While, normalmente usamos ele quando não sabemos precisamente o tamanho da str, ou seja, é variado
texto = "Python"
i = 0
While i < len(texto)
    print(texto[i], i)
    i += 1

Agora o mesmo Código pode ser implementado rapidamente com o for! 
A principal questão aqui é que sabemos precisamente o Tamanho da str

texto = "python"
novo_texto = "*"
for i in texto:
    novo_texto += i
    print(i)
print(novo_texto)
"""