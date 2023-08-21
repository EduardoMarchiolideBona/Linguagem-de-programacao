#1) Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo pelo teclado e mostra na tela o seu tipo de dado.

valor1=input(float("Digite o valor 1: "))
valor2=input(float("Digite o valor 2: "))

print(f'A soma  dos dois valores é: ', valor1 + valor2)

print(type(valor1))
print('O dado é uma letra?: ', valor1.isalpha())
print('O dado é numérico?: ', valor1.isnumeric())
print('O dado é só espaço?: ', valor1.isspace())
print('O dado é alfanumérico?: ', valor1.isalnum())
print('O dado é maiúsculo?: ', valor1.isupper())
print('O dado é minúsculo?: ', valor1.islower())
print('O dado é capitalizada?: ', valor1.istitle())