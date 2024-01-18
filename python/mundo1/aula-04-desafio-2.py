print('Preencha os dados de nascimento solicitados abaixo:')

dia = ''
mes = ''
ano = ''

while dia == '':
    dia = input('Dia de nascimento: ')

while mes == '':
    mes = input('Mes de nascimento: ')

while ano == '':
    ano = input('Ano de nascimento: ')

print(f"Você nasceu no dia {dia} de {mes} de {ano}.")
