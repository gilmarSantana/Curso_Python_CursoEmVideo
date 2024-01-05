# Faça um algoritmo que leia o preço
# de um produto e mostre seu novo
# preço com 5% de desconto

preco = float(input('Qual o preço do item? '))
desconto = float(input('Qual o desconto do item? '))
porcentagem = desconto
valor_porcentagem = porcentagem / 100
new_price = preco - (preco * valor_porcentagem)

print('O preço com {:.0f}% de desconto é {:.2f}'.format(porcentagem,new_price))


