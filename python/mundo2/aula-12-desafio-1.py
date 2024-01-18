# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
# será negado.

salario = float(input('Digite o seu salário: '))
valor_casa = float(input('Qual o valor do imóvel? '))
parcelas = int(input('Em quantos anos você deseja pagar? '))

percentage30salary = salario * (30 / 100)

valor_parcela = valor_casa / (parcelas * 12)

if valor_parcela > percentage30salary:
    print(f'Financiamento negado, pois a parcela de {valor_parcela:.2f} excederá os 30% do seu salário que é {percentage30salary}.')
else:
    print(f'Ótimo, serão {parcelas * 12} parcelas de R${valor_parcela:.2f}')