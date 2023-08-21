# 22) Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles. Desconsiderando o valor 1000 da parada.

lista=[]

while True:
    numero = int(input("DIgite um numero: "))
    if (numero == 1000):
        break
    lista.append(numero)
print(f'A quantia de numeros digitado foi {len(lista)}')
print(f'A soma de todos os números digitados foi {sum(lista)}')

