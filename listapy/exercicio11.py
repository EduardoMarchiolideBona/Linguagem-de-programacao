# 11) Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E ao final mostrar seu nome e salário final calculado.

nome = input("Digite seu nome : ")
horas = float(input("Quantas horas você trabalhou : "))
valor_horas = float(input("Digite o valor da sua hora : "))
salariobruto = horas * valor_horas
print(f'Sr(a) {nome} seu salario bruto é de {salariobruto} com o desconto do INSS : {salariobruto * 0.02} ')

