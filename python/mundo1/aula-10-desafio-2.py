# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostra uma mensagem dizendo
# que ele foi multado, a multa vai custar R$7 por
# cada Km acima do limite.

velocidade = 120
limite = 80
multa_por_km = 7

if velocidade > limite:
    multa = abs(velocidade - limite) * multa_por_km
    print('Você foi multado em R${}'.format(multa))
