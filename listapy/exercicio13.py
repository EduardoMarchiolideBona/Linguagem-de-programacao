# 13) Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles.

lista = []

for i in range(5):
    lista.append(int(f'DIgite o número {i + 1} : '))
print(f'a soma dos itens da lista é:   {sum(lista)}')
