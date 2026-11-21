print("    JOGO DO NÚMERO SECRETO    \n")

#Jogador 1
while True:
        numero_secreto = int(input("Jogador 1, insira um número entre 0 e 100: "))
        if 0<= numero_secreto <= 100:
            break
        else:
            print("ERRO: o número deve estar entre 0 e 100 inclusive!")


print("Número guardado com sucesso! Agora é a vez do Jogador 2.")
tentativas = 0

#Jogador 2
while True:
    palpite = int(input("Jogador 2, introduza o seu palpite (0-100): "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é MAIOR que o seu palpite!")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR que o seu palpite!")
    else:
        print(f"PARABÉNS! Acertou no número secreto! {numero_secreto}")
        print(f"Necessitou de {tentativas} tentativa(s) para acertar.")
        break