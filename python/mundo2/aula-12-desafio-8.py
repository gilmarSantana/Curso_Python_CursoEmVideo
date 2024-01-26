# Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e a
# condição de pagamento.
# À vista dinheiro/cheque/pix/débito: 10% de desconto
# À vista no c.c. 5% de desconto
# Em até 2x no c.c. preço normal
# 3x ou mais no c.c. 20% de juros

condicao_pagamento = 'cc'
valor_produto = 100.00
valor_a_pagar = valor_produto
parcelas = 4
desconto = 0
aumento = 0

if condicao_pagamento == 'dinheiro' or condicao_pagamento == 'cheque' or condicao_pagamento == 'pix' or condicao_pagamento == 'debito':
    desconto = valor_produto * (10 / 100)
    aumento = 0
    valor_a_pagar = valor_produto - desconto
elif condicao_pagamento == 'cc':
    if parcelas == 1:
        desconto = valor_produto * (5 / 100)
        aumento = 0
        valor_a_pagar = valor_produto - desconto
    elif parcelas == 2:
        desconto = 0
        aumento = 0
    elif parcelas > 2:
        desconto = 0
        aumento = valor_produto * (20 / 100)
        valor_a_pagar = valor_produto + aumento

print(f'{valor_a_pagar:.2f}')
