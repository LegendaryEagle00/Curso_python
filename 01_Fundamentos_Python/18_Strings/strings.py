nome = "Otavio Augusto"
print(nome)
print(type(nome))

print(nome[0])
# nome[0] = "P" # Erro, strings são imutáveis

print(nome[0:6])
print(nome[7:14])
print(nome[9:])
print(nome[:5])

print(nome[::2])
print(nome[::-1])
#[inicio:fim:passo] # Início, fim e passo são opcionais e podem ser negativos alem de que o fim não é inclusivo 


texto = 'Texto entre apostrofos pode ter "aspas"'
print(texto)
doc = """Texto com múltiplas
... linhas"""
print(doc)

doc = '''Também é possível 
... com 3 aspas simples'''
print(doc)


frase = "Python é uma linguagem excelente"
print("Python" in frase)
print("python" in frase) # Case sensitive
print("Java" in frase)
print(len(frase)) # Tamanho da string
print(frase.lower()) # Todas as letras minúsculas
print(frase.upper()) # Todas as letras maiúsculas
print(frase.split()) # Separa a string em uma lista de palavras
print(frase.split("a")) # Separa a string em uma lista de palavras, utilizando "a" como separador
print(frase.strip()) # Remove espaços em branco do início e do fim da string
print(frase.rstrip()) # Remove espaços em branco do fim da string
print(frase.lstrip()) # Remove espaços em branco do início da string
print(frase.replace("Python", "C")) # Substitui "Python" por "C"
print(frase.find("linguagem")) # Retorna a posição da palavra "linguagem"
print(frase.find("Java")) # Retorna -1 se não encontrar
print(frase.count("a")) # Conta quantas vezes a letra "a" aparece
print(frase.capitalize()) # Primeira letra maiúscula
print(frase.title()) # Primeira letra de cada palavra maiúscula
print(frase.startswith("Python")) # Verifica se a string começa com "Python"
print(frase.endswith("Python")) # Verifica se a string termina com "Python"
print(frase.isnumeric()) # Verifica se a string é numérica
print(frase.isalpha()) # Verifica se a string é alfabética
print(frase.isalnum()) # Verifica se a string é alfanumérica
print(frase.isspace()) # Verifica se a string é composta apenas por espaços
print(frase.istitle()) # Verifica se a string está em formato de título
print(frase.isupper()) # Verifica se a string está em maiúsculas
print(frase.islower()) # Verifica se a string está em minúsculas
print(frase.upper().isupper()) # Encadeamento de métodos 
print(frase.lower().islower()) 
print(frase.capitalize().istitle()) 
print(frase.title().istitle())


