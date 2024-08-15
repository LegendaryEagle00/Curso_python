for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)
    
for i in range(1, 11, 2):
    print(i)
    
for i in range(10, 0, -1):
    print(i)
    
for index, letra in enumerate('abcdefgh'):
    print(index, letra)
    

for letra in 'abcdefgh':
    print(letra)
    
palavra = 'Gavião'
for letra in palavra:
    print(letra)
    
aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)
    
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')
    

dicionario = {'nome': 'Rafaela', 'idade': 25, 'sexo': 'F'}
for chave in dicionario:
    print(chave)
    
for valor in dicionario.values():
    print(valor)
    
for chave, valor in dicionario.items():
    print(chave, valor)

#em Python as variaveis usadas no for não são destruidas após o loop
#exemplo:
print(chave,valor) #aqui a chave e o valor ainda existem
print(dia) #aqui o dia ainda existe



for x in range(1, 11):
    if x % 2 == 0:
        print(x)
    elif x== 7:
        break # o break faz com que o loop seja interrompido

for x in range(1, 11):
    if x == 7:
        continue # o continue faz com que o loop pule para a proxima iteração
    print(x)


for i in range(1, 11):
    print(i)
else:
    print('Fim!')
    
for i in range(1, 11):
    if i == 5:
        break # neste caso o else não é executado
    print(i)
else:
    print('Fim!')