# 25) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

if (usuario == senha):
    print(f'Senha invalida, a senha nao pode ser igual ao usuario!')
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")


else :
    print(f'tudo certo :)')
