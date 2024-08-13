a = 4
b = 2.4

c = a + b
print(c)
print(type(c))

c = a / b
print(c)
print(type(c))

c = a // b
print(c)
print(type(c))

c = a * b
print(c)
print(type(c))

c = a ** b
print(c)
print(type(c))

c = a % b
print(c)
print(type(c))

c = a - b
print(c)
print(type(c))

c = -a
print(c)
print(type(c))

print(b.is_integer())

print(abs(c))

print(1.1 + 2.2)
# Output: 3.3000000000000003 pq o float não é preciso em Python e o resultado é uma aproximação do valor real 3.3 


# Para resolver esse problema, podemos utilizar o módulo decimal
from decimal import Decimal, getcontext
# Precisão de 4 casas decimais
getcontext().prec = 4
print(Decimal(1.1) + Decimal(2.2))
# Output: 3.3 pq o módulo decimal permite definir a precisão dos números decimais

#outro exemplo
getcontext().prec = 10
print(Decimal(1.1) + Decimal(2.2))
print(dir(Decimal))
print(help(Decimal))
