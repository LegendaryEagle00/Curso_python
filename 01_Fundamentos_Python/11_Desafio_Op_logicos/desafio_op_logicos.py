#Desafio Operadores Lógicos
#1. Os trabalhos
trabalho_terca = True
trabalho_quinta = True

"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete
fica_em_casa = not tv50 and not sorvete

print(f'TV50={tv50} TV32={tv32} Sorvete={sorvete} Saudável={mais_saudavel} Fica em casa={fica_em_casa}')