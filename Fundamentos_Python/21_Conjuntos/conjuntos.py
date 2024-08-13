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
print(c.union(a))
print(c.intersection(a))
print(c.difference(a))
print(c.update(a))
print(c)
print(c <= a)
print(c >= a)
print(c - a)
