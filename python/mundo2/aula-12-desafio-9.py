# Crie um programa que faça o computador jogar jokempô com você
import random

jodadas_opcoes = ('pedra', 'papel', 'tesoura')

while True:
    jogada_usuario = int(input('''Informe uma das opções:
Fique tranquilo, a escolha da máquina é gerada aleatóriamente como deve ser
[0] Pedrra
[1] Papel
[2] Tesoura
---> '''))
    if jogada_usuario in (0, 1, 2):
        jogada_maquina = random.randint(0, 2)
        if ((jogada_maquina == 0 and jogada_usuario == 0) or
            (jogada_maquina == 1 and jogada_usuario == 1) or
            (jogada_maquina == 2 and jogada_usuario == 2)):
            print(f"\n VOCẼ:{jodadas_opcoes[jogada_usuario]} MÁQ:{jodadas_opcoes[jogada_maquina]}, tente novamente\n",
                  '-=' * 120)
            continue
        elif jogada_maquina == 0 and jogada_usuario == 1:
            print(f"\nVOCẼ:{jodadas_opcoes[jogada_usuario]} MÁQ:{jodadas_opcoes[jogada_maquina]}, você ganhou, parabéns\n",
                  '-=' * 120)
            break
        elif jogada_maquina == 0 and jogada_usuario == 2:
            print(f"\nVOCẼ:{jodadas_opcoes[jogada_usuario]} MÁQ:{jodadas_opcoes[jogada_maquina]}, você perdeu\n",
                  '-=' * 120)
            break
        elif jogada_usuario == 0 and jogada_maquina == 1:
            print(f"\nVOCẼ:{jodadas_opcoes[jogada_usuario]} MÁQ:{jodadas_opcoes[jogada_maquina]}, você perdeu\n",
                  '-=' * 120)
            break
        elif jogada_usuario == 0 and jogada_maquina == 2:
            print(
                f"\nVOCẼ:{jodadas_opcoes[jogada_usuario]} MÁQ:{jodadas_opcoes[jogada_maquina]}, você ganhou, parabéns\n",
                '-=' * 120)
            break
    else:
        continue

