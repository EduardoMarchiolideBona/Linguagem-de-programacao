# 23) Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a escrever valores.

lista=[]
while True:
    numero = int(input("DIgite um numero: "))
    lista.append(numero)
    opcao = int(input("continuar? 1 - sim   2 - Não"))
    if opcao == 2:
        break

print(f'a média dos valores é {sum(lista) / len(lista)}')
print(f'o maior valor da lista é {max(lista)}')
print(f'o menor valor da lista é {min(lista)}')


    




