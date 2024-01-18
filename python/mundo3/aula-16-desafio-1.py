# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso de zero até vinte.
#
# Seu programa perguntará ao usuário o número a escrever e
# mostrar o número por extenso.

extensos = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'dezesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

n_in = -1
continua = True
while continua:
    while n_in > 20 or n_in < 0:
        n_in = int(input('Digite um número entre 0 e 20: '))

    print(f'\nVocê digitou o número {str(extensos[n_in]).capitalize()}')

    if input('\nDeseja continuar? S ou N: ') == 'S':
        continua = True
        n_in = -1
    else:
        continua = False
