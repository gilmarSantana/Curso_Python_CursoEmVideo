# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'

cidade = 'Varzea Paulista'

teste = cidade[:5].upper() == 'SANTO'

if teste:
    print('Começa com SANTO')
else:
    print('Não começa com SANTO')
