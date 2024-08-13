# Conjuntos são coleções de elementos únicos, não ordenados e não indexados.
# São representados por chaves {}.

a = {1, 2, 3}
print(a)
print(type(a))
print(len(a))

# Conjuntos não aceitam elementos duplicados.
b = {1, 2, 3, 3, 3, 3, 3}
print(b)
print(len(b))

print({1, 2, 3} == {3, 2, 1, 1, 1, 1})

c = {2, 3, 4, 5} 
print(c.union(a)) # c U a
print(c.intersection(a)) # c interseção a
print(c.difference(a)) # c - a
print(c.update(a)) # c = c U a
print(c) # c = c U a
print(c <= a) # c é um subconjunto de a.
print(c >= a) # c é um superconjunto de a.
print(c - a) # Diferença entre os conjuntos.
