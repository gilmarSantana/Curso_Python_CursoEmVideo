# Desenvolva um programa que leia o comprimento das três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

import matplotlib.pyplot as plt
import numpy as np


r1 = 500
r2 = 300
r3 = 400

t1 = r1 + r2 > r3
t2 = r2 + r3 > r1
t3 = r3 + r1 > r2

if t1 and t2 and t3:
    print("Os comprimentos podem formar um triângulo.")
    print('Drawing...')

    angulo1 = np.degrees(np.arccos((r2 ** 2 + r3 ** 2 - r1 ** 2) / (2 * r2 * r3)))
    angulo2 = np.degrees(np.arccos((r1 ** 2 + r3 ** 2 - r2 ** 2) / (2 * r1 * r3)))
    angulo3 = 180 - angulo1 - angulo2

    # Define os vértices do triângulo
    vertices = np.array([[0, 0], [r1, 0], [r2 * np.cos(np.radians(angulo1)), r2 * np.sin(np.radians(angulo1))]])

    # Desenha o triângulo
    tri = plt.Polygon(vertices, edgecolor='purple')
    plt.gca().add_patch(tri)

    # Adiciona os ângulos como texto
    plt.text(vertices[0, 0] - 0.5, vertices[0, 1], f'{angulo1:.2f}°', fontsize=10)
    plt.text(vertices[1, 0] + 0.2, vertices[1, 1], f'{angulo2:.2f}°', fontsize=10)
    plt.text(vertices[2, 0] - 0.5, vertices[2, 1] - 0.2, f'{angulo3:.2f}°', fontsize=10)

    # Exibe o gráfico
    plt.axis('equal')
    plt.show()

else:
    print("Os comprimentos não podem formar um triângulo.")
