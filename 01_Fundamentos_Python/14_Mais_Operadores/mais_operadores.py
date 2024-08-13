#Operador de Membro
#O operador de membro é utilizado para verificar se um objeto é membro de uma coleção.
#Exemplo:
lista = [1, 2, 3, 4, 5]
print(1 in lista)
print("Ana" in lista)

#Operador de Identidade
#O operador de identidade é utilizado para verificar se dois objetos são iguais.
#Exemplo:
x = 3
y = 3

print(x is y)
print(y is x)

print(x is not y)

lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]
print("listas is")
print(lista1 is lista2)
print(lista2 is lista3)
print(lista3 is lista1)

print("listas is not")
print(lista1 is not lista2)
print(lista2 is not lista3)
print(lista3 is not lista1)