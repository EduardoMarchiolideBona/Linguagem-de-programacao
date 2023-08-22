# 4) Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele.

coisa = input("Digite alguma coisa")

print('O dado é uma letra?: ', coisa.isalpha())
print('O dado é numérico?: ', coisa.isnumeric())
print('O dado é só espaço?: ', coisa.isspace())
print('O dado é alfanumérico?: ', coisa.isalnum())
print('O dado é maiúsculo?: ', coisa.isupper())
print('O dado é minúsculo?: ', coisa.islower())
print('O dado é capitalizada?: ', coisa.istitle())
