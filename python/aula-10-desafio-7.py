# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a 1250 calcule um aumento de 10%
# Para os inferiores ou igual a 1250 o aumento é de 15%

salario = 4350

if salario > 1250:
    aumento = salario * (10 / 100)
else:
    aumento = salario * (15 / 100)

print('O aumento para esté é de R${}'.format(aumento), ', ficando com um novo salario de {}'.format(salario + aumento))