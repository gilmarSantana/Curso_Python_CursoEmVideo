
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = ('Arroz', 10.50, 'Feijão', 13.65, 'Açucar', 6.50, 'Macarrão', 9.00)

print('=' * 40)
print('        LISTAGEM DE PREÇOS')
print('=' * 40)

for c in range(0, len(itens), 2):
    item, preco = itens[c], itens[c+1]
    print(f'{item:.<30}', f'R$ {preco:.2f}')
print('=' * 40)
