# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria conforme a sua idade
# até 9: MIRIM
# até 14: INFANTIL
# até 19: JUNIOR
# até 20: SENIOR
# acima: MASTER

from datetime import datetime

ano_atual = datetime.now().year
nasc = 1997

idade = ano_atual - nasc

if 6 <= idade <= 9:
    print('Atleta MIRIM')
elif 10 <= idade <= 14:
    print('Atleta INFANTIL')
elif 15 <= idade <= 19:
    print('Atleta JUNIOR')
elif idade >= 20 >= idade:
    print('Atleta SENIOR')
elif idade > 20:
    print('Atleta MASTER')
else:
    print('Não pode competir devido a idade.')

