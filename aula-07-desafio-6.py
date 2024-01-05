# Crie um programa que leia quanto
# dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar

carteira = float(input('Quanto tem na sua carteira?'))
def cambio(carteira):
    dolar = 3.27

    dolar_disponivel = carteira // dolar
    restante = carteira % dolar
    if carteira < dolar or dolar_disponivel <= 0:
        return print('Saldo na carteira insuficiente para conversão.')

    return print('Você pode obter ${}, e ainda te sobra R$ {}.'.format(dolar_disponivel, restante))


cambio(carteira)