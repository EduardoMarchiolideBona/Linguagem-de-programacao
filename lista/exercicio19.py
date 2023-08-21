#  19) Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: 

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("DIgite o segundo número: "))

operacao = int(input("Digite a operação 1 - soma \n"
                                        "2 - difrença \n"
                                        "3 - produto \n"
                                        "4 - divisão "))

if (operacao == 1):
    print(f'A soma dos dois números é {numero1 + numero2}')

if (operacao == 2):
    print(f'A diferença dos dois números é {numero1 - numero2}')

if (operacao == 3):
    print(f'o produto dos dois números é {numero1 * numero2}')

if (operacao == 4):
    print(f'A divisão dos dois números é {numero1 // numero2}')

                                
                                        
