# Escreva um programa que faça o computador pensar em um número
# inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

import random

correct_answer = False

aleatory_number = random.randint(1,5)

while correct_answer is False:
    user_number_test = int(input('Adivinhe um número de 1 a 5: '))
    if aleatory_number != user_number_test:
        print('Resposta incorreta')
        print('-' * len('RAdivinhe um número de 1 a 5: '))
    else:
        print('Resposta correta.')
        correct_answer = True
print('-' * 10, 'FIM DE JOGO', '-' * 10)

