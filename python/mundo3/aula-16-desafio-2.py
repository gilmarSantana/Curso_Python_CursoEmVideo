# Crie uma tupla preechida com os 20 primeiros colocados da tabela do
# campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
tabela_brasileirao_2021 = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo", "Fluminense",
                           "Grêmio", "Palmeiras", "Santos", "Athletico Paranaense", "Bragantino",
                           "Ceará", "Corinthians", "Atlético Goianiense", "Bahia", "Sport",
                           "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")

# Apenas os cinco primeiro colocados
print('Os cinco primeiros \n', tabela_brasileirao_2021[:5], '\n', '=-' * 50)

# Os ultimos 4 colocados
print('Os quatro últimos \n', tabela_brasileirao_2021[-4:], '\n', '=-' * 50)

# Uma lista com os times em ordem alfabética
print('Os times em ordem alfabética \n', sorted(tabela_brasileirao_2021), '\n', '=-' * 50)

print(f'O Palmeiras está na {tabela_brasileirao_2021.index("Palmeiras")}° colocação, está atrás do '
          f'{tabela_brasileirao_2021[tabela_brasileirao_2021.index("Palmeiras") - 1]} e na frente do '
      f'{tabela_brasileirao_2021[tabela_brasileirao_2021.index("Palmeiras") + 1]}')

for colocacao, time in enumerate(tabela_brasileirao_2021):
    if time == 'Palmeiras':
        print(f'O {time} está na {colocacao}° colocação, está atrás do '
              f'{tabela_brasileirao_2021[colocacao - 1]} e na frente do {tabela_brasileirao_2021[colocacao + 1]}')
# Em que colocação na tabela está o time Palmeiras
