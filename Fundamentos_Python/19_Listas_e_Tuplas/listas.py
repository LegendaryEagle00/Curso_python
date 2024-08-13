lista = []

print(lista)
print(type(lista))
print(len(lista))

lista = [1, 2, 3]
print(lista)
print(len(lista))

lista.append(4) # Adiciona um elemento ao final da lista
print(lista)

lista.append("Python") # Listas podem ter elementos de tipos diferentes
print(lista)

lista.append([1, 2, 3]) # inclusive outras listas
print(lista)

lista.pop() # Remove o último elemento da lista
print(lista)

lista.remove(2) # Remove o elemento 2 da lista
print(lista)


lista.reverse() # Inverte a ordem dos elementos
print(lista)


lista2 = 10 * [0] # Cria uma lista com 10 elementos iguais a 0
print(lista2)

lista3 = [1, 2, 'Python', [3, 4], 5]
print(lista3.index('Python')) # Retorna o índice do elemento 'Python'
print(lista3.count(1)) # Conta quantas vezes o elemento 1 aparece na lista
print('Python' in lista3) # Verifica se 'Python' está na lista
print(2 in lista3)
print(2 not in lista3)

print(lista3[1:3]) # Retorna os elementos de índice 1 e 2
print(lista3[1:4]) # Retorna os elementos de índice 1, 2 e 3
print(lista3[:3]) # Retorna os elementos de índice 0, 1 e 2
print(lista3[2:]) # Retorna os elementos de índice 2 até o final
print(lista3[::2]) # Retorna os elementos de índice par
print(lista3[::-1]) # Inverte a ordem dos elementos
print(lista3[3][0]) # Retorna o primeiro elemento da sublista
print(lista3[3][1]) # Retorna o segundo elemento da sublista
print(lista3[3][::-1]) # Inverte a ordem dos elementos da sublista
