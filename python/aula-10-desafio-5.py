# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Para ser bissexto, o ano deve ser:
# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.


ano = 2024

if ano % 4 == 0:
    teste1 = True
else:
    teste1 = False

if ano % 100 == 0:
    teste2 = False
else:
    teste2 = True


if teste1 and teste2:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
