from random import random

tamanho_do_vetor_a = int(input("Digite o tamanho do vetor A: "))

vetor_a = [None] * tamanho_do_vetor_a
for i in range(len(vetor_a)):
    vetor_a[i] = float(random() * 100)

print('[', end='')
for i in range(len(vetor_a)):
    if i < len(vetor_a) - 1:
        print(f'{vetor_a[i]:.1f}, ', end='')
    else:
        print(f'{vetor_a[i]:.1f}', end='')
print(']')

tamanho_do_vetor_b = int(input("Digite o tamanho do vetor B: "))

vetor_b = [None] * tamanho_do_vetor_b
for i in range(len(vetor_b)):
    vetor_b[i] = float(random() * 100)

print('[', end='')
for i in range(len(vetor_b)):
    if i < len(vetor_b) - 1:
        print(f'{vetor_b[i]:.1f}, ', end='')
    else:
        print(f'{vetor_b[i]:.1f}', end='')
print(']')


C = [[0] * len(vetor_b) for _ in range(len(vetor_a))]

for i in range(len(vetor_a)):
    for j in range(len(vetor_b)):
        C[i][j] = vetor_a[i] * vetor_b[j]


print("Matriz resultante C:")
for linha in C:
    print(linha)