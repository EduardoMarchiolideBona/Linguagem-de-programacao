# 8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura em metros: "))

print(f'A área é {largura * altura}')
print(f'Você precisará de  {(largura * altura) / 2} litros de tinta')
