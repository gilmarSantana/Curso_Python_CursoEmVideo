# Crei um programa que tenha uma tupla com várias palavras (não user acentos)
# Depois disso, você deve mostrar para cada palavra quais são as suas vogais

vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

palabras = ('abacaxi', 'cachorro', 'elefante', 'girassol', 'computador', 'montanha', 'ocelote', 'telescopio',
            'frutas', 'bicicleta', 'relampago', 'biblioteca', 'espelhamento', 'ventilador', 'planeta', 'chocolate',
            'diamante', 'galaxia', 'sorvete')


for p in palabras:
    print(f'\nNa palabra {p} temos', end='')
    for v in p:
        if v in vogais:
            print(v, end=' ')