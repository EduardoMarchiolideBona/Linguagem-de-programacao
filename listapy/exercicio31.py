# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.

import random
cont_vitoria = 0
while True:
    jogador = input("Escolha par ou ímpar (P/I): ").upper()
        
    if (jogador != 'P') and (jogador != 'I'):
            print("Escolha inválida. Digite 'P' para par ou 'I' para ímpar.")
            jogador = input("Escolha par ou ímpar (p/i): ").upper()
              
    n_jogador = int(input("Digite um número entre 0 e 10: "))
    if (n_jogador < 0) or (n_jogador > 10):
            print("Número inválido. Digite um número entre 0 e 10.")
            n_jogador = int(input("Digite um número entre 0 e 10: "))
            
        
    numero_pc = random.randint(0, 10)
    soma = n_jogador + numero_pc

    if (jogador == "P"):
          if (soma % 2 == 0):
                 print(f'Voce venceu')
                 cont_vitoria += 1
    
    if (jogador == "I"):
           if (soma % 2 == 0):
                  print(f'voce perdeu')
           

    print(f"Você escolheu {n_jogador} e o computador escolheu {numero_pc}.")
    print(f"A soma dos números é {soma}.")