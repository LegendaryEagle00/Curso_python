tupla = tuple()
# ou 
tupla = ()
print(type(tupla))
#tupla = ('um') # Isso não é uma tupla
tupla = ('um',) # Isso é uma tupla
print(type(tupla))
#tupla[0] = 1 # Erro, tuplas são imutáveis
#tupla.append(2) # Erro, tuplas são imutáveis
print(len(tupla))