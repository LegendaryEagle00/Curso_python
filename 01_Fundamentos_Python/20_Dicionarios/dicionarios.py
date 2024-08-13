variavel2 = "variavelTeste"
dicionario = {"nome": "Python", "versao": 3.8, variavel2 : "teste"}
print(dicionario)
print(dicionario["nome"])
print(dicionario["versao"])
dicionario["versao"] = 3.9
print(dicionario)
dicionario["site"] = "python.org"
print(dicionario)
del dicionario["site"]
print(dicionario)
print(len(dicionario))
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
print("nome" in dicionario)
print("site" in dicionario)


pessoa = {"nome": "Lucas", "idade": 25, "cidade": "São Paulo"}
print(pessoa)
pessoa["idade"] = 26
print(pessoa)

pessoa["pais"] = "Brasil"
print(pessoa)

pessoa.pop("cidade")
print(pessoa)

pessoa.update({"cidade": "Rio de Janeiro"})
print(pessoa)

pessoa.clear()
print(pessoa)
