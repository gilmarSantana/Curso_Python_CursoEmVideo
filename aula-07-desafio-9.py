# Faça um algoritmo que leia o salário
# de um funcionário e mostre seu novo
# salário com 15% de aumento

salario = float(input('Qual o salário? '))
porcentagem_aumento = float(input('Qual a porcentagem de aumento? '))
valor_porcentagem = porcentagem_aumento / 100
novo_salario = salario + (salario * valor_porcentagem)

print('Você passou de ganhar {} para ganhar {}'.format(salario, novo_salario))
