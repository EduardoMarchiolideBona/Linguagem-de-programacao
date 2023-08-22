# 7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.

preco = float(input("Digite quantos reias custa o produto: "))

print(f'o valor com 5% de desconto é {preco - (preco * 0.05)}')
print(f'o valor com 15% de aumento é {preco + (preco * 0.15)}')
