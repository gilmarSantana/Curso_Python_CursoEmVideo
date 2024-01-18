# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando 0,50 por KM para viagens de até
# 200km e 0,45 para viagens mais longas

distancia_viagem = 600

if distancia_viagem <= 200:
    taxa = 0.50
else:
    taxa = 0.45

print('O preço da passagem é R${:.2f}'.format(distancia_viagem * taxa))