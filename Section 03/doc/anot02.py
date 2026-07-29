#variavel_a = 10 or 20
#variavel_b = 1 or 1

#print(variavel_a, variavel_b)

#Notação - Interpolação de str, preferível o Fstring
name = "luiz"
price = 100.21203
test = "%s, o preço é %.2f" % (name, price)
#Isso se chama Interpolação de string, funciona similar ao format, só que pra chamar tem que ter o % (variavel 1, variavel2 ....)
# %s == String ; %f == Float ; %i == Int ; %b == Booleirano.
print(test)