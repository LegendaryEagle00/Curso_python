import random

def sortear_dado():
    return random.randint(1, 6)

while True:
    dado = sortear_dado()
    print(dado)
    if dado == 6:
        break
    
while True:
    resposta = input('Gostaria de jogar o dado? (s/n) ')
    if resposta in ['s', 'S']:
        print(sortear_dado())
    else:
        break
    
dado_sorteado = sortear_dado()
numero_informado = 0
while numero_informado != dado_sorteado:
    numero_informado = int(input('Informe um número: '))
    if numero_informado > 6 or numero_informado < 1:
        print('Número inválido. Você deve informar um número de 1 a 6.')
        continue