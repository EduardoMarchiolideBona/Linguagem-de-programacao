# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
total_compra = 0
while True:
    preco = float(input("Digite o preço da mercadoria (0 para encerrar): "))
    if preco == 0:
        break
    total_compra += preco
    print(f'o total da compra é de {total_compra}')
    dinheiro = float(input("Digite a quantia que você irá dar: "))
    print(f'o troco é de {total_compra - dinheiro}')
    