# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# Se ele ainda vai se alistar
# Se é a hora de se alistar
# Se já passou do tempo de se alistar
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

# A obrigação para com o Serviço Militar, em tempo de paz, começa no 1º dia de janeiro do ano em que o cidadão completar
# 18 (dezoito) anos e subsistirá até 31 de dezembro do ano em que completar 45 (quarenta e cinco) anos.

ano_atual = datetime.now().year
ano_nascimento = 1970
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f'Ainda não chegou a hora de se alistar pois você ainda não completou 18 anos, ainda falta'
          f'{18 - idade} anos para o seu alistamento militar')
elif idade == 18:
    print(f'Você tem {idade} e está na hora de se alistar')
elif 18 < idade <= 45:
    print(f'Passou da hora de se alistar, pois você já tem {idade} anos, você está {idade - 18} anos atrasado')
else:
    print(f'Com a idade de {idade} anos vocẽ está desobrigado do alistamento militar')
