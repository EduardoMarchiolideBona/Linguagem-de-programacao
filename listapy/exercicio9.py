#9) Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.

nome = input("Digite seu nome : ")
carteira = float(input("Digite quantos reias você tem na carteira: "))

print(f'Você pode comprar {carteira / 5.41} dollares')
print(f'Você pode comprar {carteira / 5.43} Euros')