"""
Projeto de jogo de adivinhação
"""

print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

NUMERO_SECRETO = 77

chute = int(input("Digite o seu numero:"))

print("Voce digitou", chute)

ACERTOU = chute == NUMERO_SECRETO
NUMERO_MAIOR = chute > NUMERO_SECRETO
NUMERO_MENOR = chute < NUMERO_SECRETO

if ACERTOU:
    print("Parabéns, voce acertou")
else:
    if NUMERO_MAIOR:
        print("Seu chute foi maior que o número secreto")
    elif NUMERO_MENOR:
        print("Seu chute foi menor que o número secreto")

print("Fim do jogo")
