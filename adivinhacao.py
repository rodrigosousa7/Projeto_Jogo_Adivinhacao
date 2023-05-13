"""
Projeto de jogo de adivinhação
"""

print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

NUMERO_SECRETO = 77
TOTAL_DE_TENTATIVAS = 3
RODADA = 1

for RODADA in range(1, TOTAL_DE_TENTATIVAS + 1):
    print(f"Tentativa {RODADA} de {TOTAL_DE_TENTATIVAS}")
    print()

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Voce digitou --->", chute)
    print()

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        print()
        continue

    ACERTOU = chute == NUMERO_SECRETO
    NUMERO_MAIOR = chute > NUMERO_SECRETO
    NUMERO_MENOR = chute < NUMERO_SECRETO

    if ACERTOU:
        print("Parabéns, voce acertou!")
        print()
        break
    else:
        if NUMERO_MAIOR:
            print("Seu chute foi maior que o número secreto")
            print()
        elif NUMERO_MENOR:
            print("Seu chute foi menor que o número secreto")
            print()

print("Fim do jogo")
