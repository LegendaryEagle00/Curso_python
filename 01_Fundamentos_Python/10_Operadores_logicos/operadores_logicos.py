print(7 != 7) # False
print(7 <  8) # True

print(7 != 7 and 7 > 8) # False and False = False
print( 7 == 7 and 7 > 8) # True and False = False
print( 7 == 7 and 7 < 8) # True and True = True

print(7 != 7 or 7 < 8) # False or True = True
print(7 == 7 or 7 < 8) # True or True = True
print(7 != 7 or 7 > 8) # False or False = False

print(not False) # True
print(not True) # False

print(not not True) # True
print(not not False) # False


saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0
print(meta) # True