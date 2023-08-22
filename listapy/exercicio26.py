# 26) Faça um programa que leia e valide as seguintes informações:

nome = input("Digite seu nome: ")
if (len(nome) < 3):
    print(f'O nome tem que ter mais de 3 caracteres')

idade = int(input("Digite sua idade: "))
if (idade > 150):
    print(f'sua idade tem que estar entre 0 a 150')

salario = float(input("Digite seu salario: "))
if (salario < 0):
    print(f'seu salario tem q ser mais de 0')

sexo = input("Digite seu sexo ('F' ou 'M'): ").upper()
if (sexo != 'F') or (sexo != 'M'):
    print(f'Digite um sexo VALIDO!!!!!!!!!!!!')

ec = input("Digite seu estado civil ('s', 'c', 'v', 'd')").lower()
if (ec != 's', 'c', 'v', 'd'):
    print(f'DIgite um estado civil valido')





